# mask-multilabel-classifiaction-model
사람 사진에서 마스크 착용 유무, 성별, 나이를 분류하는 Multi-label classification model

## :floppy_disk: 데이터
train set : company 별 job과 규모    
<img src="https://user-images.githubusercontent.com/43736669/94919776-fcce3780-04ef-11eb-8217-5b24a8303fef.png">  
job_tags.csv : job 별 tag  (job에 대응되는 기술)  
<img src="https://user-images.githubusercontent.com/43736669/94920971-4f105800-04f2-11eb-8041-37ad4d791527.png">  
valid set : tag 별 기술 이름 (기술 태그 Hash에 대응되는 이름)  
<img src ="https://user-images.githubusercontent.com/43736669/94921035-6e0eea00-04f2-11eb-9d67-c31336c783f2.png">  
user_tags.csv : user 별 관심 기술 목록  
<img src ="https://user-images.githubusercontent.com/43736669/94921123-9860a780-04f2-11eb-8d6c-5f192d35c645.png">  
train.csv(train set) : user가 해당 job에 지원하였는지 여부  
<img src ="https://user-images.githubusercontent.com/43736669/94921312-086f2d80-04f3-11eb-8256-c0e9c5cab12a.png">  

## :thought_balloon:파생 데이터
1) 회사의 규모 
미기입 : none  
10명 이하 : small   
10명 이상 100명 이하 : medium   
100명 이상 : big  
job_company로부터 추출  
 
2) weighted graph
개발자가 등록하지 않았지만 현재 기술스택과 관련도가 높은 기술을 구하기 위해 각 기술마다 다른 기술과의 연관도를 저장한 weighted graph.  
user_tag로부터 추출  
  
3) minorstacks   
내가 보유한 기술과 연관이 높은 기술 top 10. 위의 weighted graph로부터 도출  
  
4) 일치 majorstacks  
회사에서 요구한 기술과 내가 보유한 기술의 일치 수  
  
5) 일치 minorstacks  
회사에서 요구한 기술과 내가 보유한 minorstacks의 일치 수   

6) majorstacks/companystacks, minorstacks/ companystacks   
majorstack,minorstack 일치 수 / 회사에서 요구한 기술의 수   
  
7) majorstacks/mystacks   
majorstack 일치 수 / 내가 등록한 기술 수  

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

## :chart_with_downwards_trend: Future Work
- VS Code 등 IDE 사용
- Tensorboard, wandb등 학습 관리 툴 사용
- soft ensemble, soft labeling, TTA 등 다양한 기법 사용
- 스파게티 코드 개선
- logging
- 다양한 backbone 사용

## :computer: 기술 스택  
python,jupyter notebook, numpy, pandas, pytorch
