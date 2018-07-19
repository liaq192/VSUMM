import torch
import sys
import numpy as np
from skimage import measure as mp;


def compute_reward(seq, actions, ignore_far_sim=True, temp_dist_thre=20, use_gpu=False):
    """
    Compute diversity reward and representativeness reward

    Args:
        seq: sequence of features, shape (1, seq_len, dim)
        actions: binary action sequence, shape (1, seq_len, 1)
        ignore_far_sim (bool): whether to ignore temporally distant similarity (default: True)
        temp_dist_thre (int): threshold for ignoring temporally distant similarity (default: 20)
        use_gpu (bool): whether to use GPU
    """
    _seq = seq.detach()
    # print('_seq', _seq.size());
    numpy_seq= _seq.numpy();
    # print('_seq_numpy',_seq.numpy().shape);
    a2dSeq=np.squeeze(numpy_seq,axis=0)
    # print('a2Dseq: ',a2dSeq.shape);

    _actions = actions.detach()
    pick_idxs = _actions.squeeze().nonzero().squeeze()
    # print('Picks/Indexes:, ', pick_idxs.shape[0]);
    num_picks = len(pick_idxs) if pick_idxs.ndimension() > 0 else 1
    
    if num_picks == 0:
        # give zero reward is no frames are selected
        reward = torch.tensor(0.)
        if use_gpu: reward = reward.cuda()
        return reward
    
    selectedFrames= a2dSeq[pick_idxs,:];
    # print('Selected Frames Shape:, ', selectedFrames.shape);

    ssim_score_list= [ mp.compare_ssim(selectedFrames[i][:],selectedFrames[i+1][:]) for i in range(selectedFrames.shape[0]-1)  ];
    ssim_score= reduce(lambda x, y: x + y, ssim_score_list) / len(ssim_score_list)


    _seq = _seq.squeeze()
    n = _seq.size(0)

    # compute diversity reward
    if num_picks == 1:
        reward_div = torch.tensor(0.)
        if use_gpu: reward_div = reward_div.cuda()
    else:
        normed_seq = _seq / _seq.norm(p=2, dim=1, keepdim=True)
        dissim_mat = 1. - torch.matmul(normed_seq, normed_seq.t()) # dissimilarity matrix [Eq.4]
        dissim_submat = dissim_mat[pick_idxs,:][:,pick_idxs]
        if ignore_far_sim:
            # ignore temporally distant similarity
            pick_mat = pick_idxs.expand(num_picks, num_picks)
            temp_dist_mat = torch.abs(pick_mat - pick_mat.t())
            dissim_submat[temp_dist_mat > temp_dist_thre] = 1.
        reward_div = dissim_submat.sum() / (num_picks * (num_picks - 1.)) # diversity reward [Eq.3]

    # compute representativeness reward
    dist_mat = torch.pow(_seq, 2).sum(dim=1, keepdim=True).expand(n, n)
    dist_mat = dist_mat + dist_mat.t()
    dist_mat.addmm_(1, -2, _seq, _seq.t())
    dist_mat = dist_mat[:,pick_idxs]
    dist_mat = dist_mat.min(1, keepdim=True)[0]
    #reward_rep = torch.exp(torch.FloatTensor([-dist_mat.mean()]))[0] # representativeness reward [Eq.5]
    reward_rep = torch.exp(-dist_mat.mean())

    # print('Reward_rep: ',reward_rep);
    # print('reward_div:', reward_div);
    # print('reward_att',ssim_score);
    # combine the two rewards
    # reward = (reward_div + reward_rep) * 0.5
    # reward = (reward_div + ssim_score) * 0.5
    t_ssim_score= torch.tensor(ssim_score);
    # print('reward_div: ', reward_div, '  t_ssim_score: ',t_ssim_score);
    reward = (reward_div + t_ssim_score) * 0.5    
    return reward
