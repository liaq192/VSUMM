
<div align="center">
  <img src="imgs/pipeline.jpg" alt="train" width="80%">
</div>

## Reward=  Reward_Diversity + Reward_Representativeness.

where 
  #Reward_Representativeness = Pixel Difference between two consecutive images ( MSE between them)
  
  
My idea 
  #Reward_Representativeness = SSIM between two consecutive images 
  
  Where 
  
  SSIM : structural similarity (SSIM) index
  
  luminance (light emitted) , contrast( difference b/w luminance) , image degradation()


## Results : 

New Metric

| No. | Video |  F-score | <br />
| --- | -------- | ------- | <br />
| 1 | video_14 | 28.4% | <br />
| 2 | video_19 | 60.8% | <br />
| 3 | video_23 | 58.3% | <br />
| 4 | video_25 | 55.3% | <br />
| 5 | video_7 |  29.2% | <br />


| No. | Video |  F-score | <br />
| --- | -------- | ------- | <br />
| 1 | video_10 | 26.5% | <br />
| 2 | video_19 | 60.8% | <br />
| 3 | video_23 | 58.3% | <br />
| 4 | video_25 | 55.3% | <br />
| 5 | video_6 |  21.0% | <br />


| No. | Video |  F-score | <br />
| --- | -------- | --- | <br />
| 1 | video_13 | 29.2% |<br />
| 2 | video_16 | 34.9% |<br />
| 3 | video_24 | 29.5% |<br />
| 4 | video_3 |  35.2% |<br />
| 5 | video_4 |  54.4% |<br />
--- | -------- | ------- |<br />


Orignal Metric

No. | Video |  F-score | <br />
1 | video_14 | 28.4%  | <br />
2 | video_19 | 28.6% | <br />
3 | video_23 | 61.7% | <br />
4 | video_25 | 55.3% | <br />
5 | video_7 |  29.1% | <br />
--- | -------- | ------- | <br />

--- | -------- | ------- | <br />
No. | Video |  F-score | <br />
1 | video_10 | 26.5% | <br />
2 | video_19 | 28.6% | <br />
3 | video_23 | 61.7% | <br />
4 | video_25 | 55.3% | <br />
5 | video_6 |  21.0% | <br />
--- | -------- | ------- | <br />

No. | Video |  F-score | <br />
--- | -------- | ------- | <br />
1 | video_13 | 50.2% | <br />
2 | video_16 | 34.9% | <br />
3 | video_24 | 29.5% | <br />
4 | video_3 |  35.2% | <br />
5 | video_4 |  47.7% | <br />
--- | -------- | ------- | <br />
