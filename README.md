# mask-multilabel-classifiaction-model
사람 사진에서 마스크 착용 유무, 성별, 나이를 분류하는 Multi-label classification model

## :floppy_disk: 데이터
train set : 10대 ~ 60대의 마스크 착용, 미착용, 오착용(턱스크 등) 남녀 사진 12600장 및 연령, 성별 정보   
test set : 10대 ~ 60대의 마스크 착용, 미착용, 오착용(턱스크 등) 남녀 사진 
 
## :computer: 모델   
- Architecture  
![image](https://user-images.githubusercontent.com/43736669/114355181-20162580-9baa-11eb-820f-70a78cda2f35.png) 

- Multiple outputs 사용  
![image](https://user-images.githubusercontent.com/43736669/114355206-286e6080-9baa-11eb-8c5a-a3f62725594f.png)  
Mask, Gender, Age를 예측하는 3개의 모듈을 만들어 각각의 loss를 weighted sum한 값을 최종 loss로 사용   

- Loss   
![image](https://user-images.githubusercontent.com/43736669/114355314-49cf4c80-9baa-11eb-82c2-96a74b7a4ed4.png)  
Focal loss, Class-balance Loss 병합 사용(Class imbalance를 해결하기 위해)  

![image](https://user-images.githubusercontent.com/43736669/114355547-8ef37e80-9baa-11eb-921f-5bac31e2c98d.png)  
세 모듈의 loss를 weighted sum(Age를 잘 못맞출 때 penalty 부과)  

- Scheduler, Optimizer
![image](https://user-images.githubusercontent.com/43736669/114355611-a2064e80-9baa-11eb-8616-c23875f5ac9c.png)  
CosineAnealingWarmRestarts, SGD 사용   

- Data Augmentation   
Horizontal Flip, Center Crop, RandomRotation 사용  

## :chart_with_downwards_trend: Train  
![image](https://user-images.githubusercontent.com/43736669/114355975-088b6c80-9bab-11eb-8623-748124bb1920.png)  
10 fold stratified cross validation 사용(10개의 모델에 대해 Hard voting)  
![image](https://user-images.githubusercontent.com/43736669/114356075-28229500-9bab-11eb-90e3-647dcde33173.png)  
각 fold의 최종 모델은 validation의 최저 loss를 가지는 모델로 선정  

## :thought_balloon: Future Work  
- VS Code 등 IDE 사용  
- Tensorboard, wandb등 학습 관리 툴 사용  
- soft ensemble, soft labeling, TTA 등 다양한 기법 사용
- 스파게티 코드 개선
- logging
- 다양한 backbone 사용

## :computer: 기술 스택  
python,jupyter notebook, numpy, pandas, pytorch
