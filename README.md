# 🏋️‍♂️AI_Fit🏋️‍♀️

### AIFit(아이핏)은 A.I Fittness 즉 인공지능을 활용한 피트니스라는 의미입니다.

- 로그인시, **Facial recognition 기술**을 활용하여 등록된 회원 확인
- 운동시, **Pose Estimation 기술**을 활용하여 특정 운동의 자세를 학습하고 인공지능 트레이너 서비스 제공

---
### 👨‍👩‍👨‍👩‍👨‍AI_Fit 팀원
- :octocat: [이종화](https://github.com/rootsj)(팀장)
> django 유저모델 form, 정보수정 페이지, 페이스로그인 페이지 및 기능, 깃허브 관리, 버전관리, 각 팀원 일정관리, 품질 및 이슈 관리, 서류 작업

- :octocat: [김용수](https://github.com/jzqioipst)
> AWS EC2 총괄, 백엔드 총괄 작업 및 구현, 프론트 페이지(여러가지 기능들 구현: DB로부터 필요 정보 받아와서 알맞은 Chart동작 기능 구현 등). 웹개발 팀원들이 구현한 전반적인 기능 확인 및 디버깅

- :octocat: [김순영](https://github.com/s00ny0ung)
> FaceNet API, PoseNet API 및 tensorflow와 keras를 활용하여 모델 작성, 학습, 평가, 수정 및 배포, AWS SageMaker, S3 활용, 관련 신경망 모델 비교 분석, 추가 데이터 수집(동양인 데이터 - AFAD(8만장), 구글/네이버 크롤링 이용하여 연예인 사진 수집(2000장)) 및 데이터  클렌징, Teachable Machine 활용 (Squat 담당)

- :octocat: [양희영](https://github.com/rickcmc02) 
> AWS EC2 Django 배포 및 테스트, 웹 총괄 CSS 구현, 운동정보 chart.js 적용, sports.html 운동 페이지 코드 구현, static 컨텐츠 및 디렉토리 관리, pose estimation model 코드 type별 모듈화 작업, 이미지 데이터 클렌징, 서류 작업 및 ppt작업, 디자인 작업

- :octocat: [김지수](https://github.com/Jaykay2020) 
> FaceNet API, PoseNet API 및 tensorflow와 keras를 활용하여 모델 작성, 학습, 평가, 수정 및 배포, AWS SageMaker, S3 활용, 관련 신경망 모델 비교 분석, 추가 데이터 수집(동양인 데이터 - AFAD(8만장), 구글/네이버 크롤링 이용하여 연예인 사진 수집(2000장)) 및 데이터  클렌징, Teachable Machine 활용 (Armcurl 담당)

---
## 🕵️‍♂️AI_Fit 소개

### 🔎 목적
코로나19로 인해 비대면 시장은 급속도로 성장하고 있다. 앞으로 더 활성화 될 비대면 서비스에 최적화된 셀프 트레이닝 서비스를 제공하는 것이 목적이다.

### 🔎 기대효과
1. 운동시설을 방문하지 않아도 내 집에서 ‘AI_trainer’에게 관리 받을 수 있다.
2. 시각적으로 운동 자세를 보여주고, 음성안내에 따라 운동 자세가 올바른 지 파악할 수 있다. 
3. ‘AI_Fit' 음성을 통해 운동 횟수를 체크해주기 때문에 운동에 집중할 수 있다.
![img1](https://user-images.githubusercontent.com/9804248/103353360-fd289f80-4aeb-11eb-8477-d2916d1d9fa1.png)

### 🔎 Facial recognition
- CNN을 활용한 얼굴 인식 딥러닝 모델 **FACENET**을 활용함
- FACENET 문제점 : 아시아인을 대상으로 테스트 시, 인식률이 현저히 떨어지는 문제
  - 해결1 : training dataset에 아시아인 샘플 수를 늘림
  - 해결2 : classification layer 학습(KNeighborsClassification 모델)

![image](https://user-images.githubusercontent.com/9804248/103354902-25b29880-4af0-11eb-9a68-21950a550b07.png)

### 🔎 Facial recognition 웹페이지 동작 구조
![image](https://user-images.githubusercontent.com/9804248/103354443-e768a980-4aee-11eb-961e-2eed1711cb41.png)

### 🔎 Pose Estimation
- Google **Teachable Machine** 서비스 중 Pose를 활용하여 포즈 인식 모델을 구현
- Pose 인식 모델은 PoseNet과 pretrained weights 활용, javascript을 활용하여 웹서비스 구현

### 🔎 Pose Estimation 웹페이지 동작 구조
![image](https://user-images.githubusercontent.com/9804248/103355185-fe100000-4af0-11eb-9a5d-68fa1cbd34d8.png)

---
## 🕵️‍♂️AI_Fit 시연
- Facial recognition
![image](https://user-images.githubusercontent.com/9804248/103356513-63b1bb80-4af4-11eb-8e8a-941df29280bf.png)
- Pose Estimation
![img2](https://user-images.githubusercontent.com/9804248/103356865-31ed2480-4af5-11eb-9801-2a48e6737d96.png)

