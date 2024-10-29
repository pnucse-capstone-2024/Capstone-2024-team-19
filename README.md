### 1. 프로젝트 소개
#### 1.1. 배경 및 필요성
> 최근 인공지능 기술의 발전으로 음성인식 기술인 STT (Speech-To-Text) 모델이 다양하게 개발되었다. STT란 사람이 말하는 음성 언어를 컴퓨터가 해석하여 텍스트로 변환하는 처리를 의미한다. 이는 회의록 작성, 유튜브 자막 생성, 상담 기록, 음성 명령어 처리, 청각 장애인들의 학습권 보장 등 다양한 분야에서 활용되고 있다.
우리는 이러한 최신 STT를 이용하여 다중화자 기능을 추가함으로써 위의 효과와 더불어 추가적인 효용을 기대할 수 있다. 예를 들어 다중화자 인식에 대한 알고리즘 학습과 그에 대한 심화를 생각 해 볼 수 있다. 

#### 1.2. 목표 및 주요 내용
> 다중화자 기술을 기존의 학습되어진 모델을 사용하지 않고 구현한다. 이 목표를 이루기 위해서 먼저 라벨링이 된 데이터셋을 받아 모델을 학습을 시키고, 이 학습된 모델을 이용해 화자 예측을 한다. 그리고 기존 STT 기술을 사용해 음성 파일을 대화록으로 바꾸어서 화자 정보와 대화 내용을 출력한다. 이 기술을 이용해 회의나 일상 대화의 자동 대화록 생성 기능을 하는 애플리케이션을 개발하고 모델 별 성능을 측정해본다.

### 2. 상세설계
#### 2.1. 시스템 구성도
>
<img src="https://github.com/user-attachments/assets/aba26f99-6099-4456-9042-09146ddcc36b" alt="전체 구성도" width="600" />

#### 2.1. 사용 기술
> Window와 Ubuntu 환경 2가지 모두 사용하였다.
> 
> window 환경:
> window11 home
> python 3.11.9
> pytorch 2.4.0
> CUDA 12.6
> VScode 1.94.2
> GPU는 NVIDIA GeForce RTX 4070 TI
>
> Ubuntu 환경:
> Ubuntu 22.04.5
> python 3.10.12
> pytorch 2.6.0
> ROCm 6.2.2
> VScode 1.94.1
> GPU AMD Radeon RX 6700 XT


### 3. 설치 및 사용 방법
> 1. git clone을 이용하여 이 레포지토리의 파일을 받는다.
> 2. training할 wav 파일들과 json파일들을 한 폴더에 집어넣고 경로를 doDiarization.py 내 FILES_FOR_LEARNING_PATH 에 할당해준다.
> 3. training()의 주석을 해제하고 predict()를 주석처리한다
> 4. 실행하여 모델을 학습 시킨다.
> 5. 예측을 하려는 파일의 경로를 FILES_FOR_PREDICT_PATH 에 할당하고, training()을 주석 처리한 다음 predict()를 실행한다.
> 6. 결과는 터미널에 나오고, ./whisperDiarizationOutput.txt에 txt 파일로 저장된다.

### 4. 소개 및 시연 영상
> https://www.youtube.com/watch?v=rubRGvQCn1E&list=PLFUP9jG-TDp-CVdTbHvql-WoADl4gNkKj&index=19
> [![유튜브 링크](https://img.youtube.com/vi/rubRGvQCn1E&list=PLFUP9jG-TDp-CVdTbHvql-WoADl4gNkKj&index=19/0.jpg)]

### 5. 팀 소개
> 팀원 소개 & 구성원 별 역할 분담 & 간단한 연락처를 작성하세요.
>
> 변상윤 zxc6147@pusan.ac.kr
> 배경지식 학습, 상용 API 비교 및 선정, 데이터 전처리, 다중화자 뼈대 구현, UIS-RNN을 이용한 모델 학습, 보고서 작성, 발표 및 시연 준비
>
> 문성필 msp0201@pusan.ac.kr
> 배경지식 학습, 상용 API 비교 및 선정, 다중화자 구현 방법 탐구, UIS-RNN을 이용한 모델 학습, Flutter 애플리케이션 제작, 보고서 작성, 발표 및 시연 준비


