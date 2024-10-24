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
> 프로젝트에 대한 소개와 시연 영상을 넣으세요.

### 5. 팀 소개
> 팀원 소개 & 구성원 별 역할 분담 & 간단한 연락처를 작성하세요.
>
> 변상윤 zxc6147@pusan.ac.kr
> 배경지식 학습, 상용 API 비교 및 선정, 데이터 전처리, 다중화자 뼈대 구현, UIS-RNN을 이용한 모델 학습, 보고서 작성, 발표 및 시연 준비
>
> 문성필 msp0201@pusan.ac.kr
> 배경지식 학습, 상용 API 비교 및 선정, 다중화자 구현 방법 탐구, UIS-RNN을 이용한 모델 학습, Flutter 애플리케이션 제작, 보고서 작성, 발표 및 시연 준비





























Commit Test

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/NJK_cPkH)
# Template for Capstone
이 레파지토리는 학생들이 캡스톤 프로젝트 결과물을 위한 레파지토리 생성시에 참고할 내용들을 담고 있습니다.
1. 레파지토리 생성
2. 레파지토리 구성
3. 레파지토리 제출 
4. README.md 가이드라인
5. README.md 작성팁

---

## 1. 레파지토리 생성
- [https://classroom.github.com/a/NJK_cPkH](https://classroom.github.com/a/NJK_cPkH)
- 위 Github Classroom 링크에 접속해 본인 조의 github 레파지토리를 생성하세요.
<img src="https://github.com/user-attachments/assets/b5a7f34a-e146-4253-b57d-672737a75a50" alt="깃헙 클래스룸 레포 생성" width="600" />

- 레포지토리 생성 시 팀명은 `TEAM-{조 번호}` 형식으로 생성하세요.
- 예를 들어, 2024년도 3조의 팀명은 `TEAM-03` 입니다.
- 이 경우 `Capstone2024-TEAM-03`이란 이름으로 레파지토리가 생성됩니다.

---

## 2. 레파지토리 구성
- 레파지토리 내에 README.md 파일 생성하고 아래의 가이드라인과 작성팁을 참고하여 README.md 파일을 작성하세요. (이 레파지토리의 SAMPLE_README.md 참조)
- 레파지토리 내에 docs 디렉토리를 생성하고 docs 디렉토리 내에는 과제 수행 하면서 작성한 각종 보고서, 발표자료를 올려둡니다. (이 레파지토리의 docs 디렉토리 참조)
- 그 밖에 레파지토리의 폴더 구성은 과제 결과물에 따라 자유롭게 구성하되 가급적 코드의 목적이나 기능에 따라 디렉토리를 나누어 구성하세요.

---

## 3. 레파지토리 제출 

- **`[주의]` 레파지토리 제출**은 해당 레파지토리의 ownership을 **학과 계정**으로 넘기는 것이므로 되돌릴 수 없습니다.
- **레파지토리 제출** 전, 더 이상 수정 사항이 없는지 다시 한번 확인하세요.
- github 레파지토리에서 Settings > General > Danger zone > Transfer 클릭
  <img src="https://github.com/user-attachments/assets/cb2361d4-e07e-4b5d-9116-aa80dddd8a8b" alt="소유주 변경 경로" width="500" />
  
- [ Specify an organization or username ]에 'PNUCSE'를 입력하고 확인 메세지를 입력하세요.
  <img src="https://github.com/user-attachments/assets/7c63955d-dcfe-4ac3-bdb6-7d2620575f3a" alt="소유주 변경" width="400" />

---







## 4. README.md 가이드 라인
- README 파일 작성시에 아래의 5가지 항목의 내용은 필수적으로 포함해야 합니다.
- 아래의 5가지 항목이외에 프로젝트의 이해를 돕기 위한 내용을 추가해도 됩니다.
- SAMPLE_README.md 이 단순한 형태의 예제이니 참고하세요.

```markdown
### 1. 프로젝트 소개
#### 1.1. 배경 및 필요성
> 프로젝트를 실행하게 된 배경 및 필요성을 작성하세요.

#### 1.2. 목표 및 주요 내용
> 프로젝트의 목표 및 주요 내용을 작성하세요.

### 2. 상세설계
#### 2.1. 시스템 구성도
> 시스템 구성도(infra, front, back등의 node 간의 관계)의 사진을 삽입하세요.

<img src="https://github.com/user-attachments/assets/aba26f99-6099-4456-9042-09146ddcc36b" alt="전체 구성도" width="600" />

#### 2.1. 사용 기술
> 스택 별(backend, frontend, designer등) 사용한 기술 및 버전을 작성하세요.
> 
> ex) React.Js - React14, Node.js - v20.0.2

### 3. 설치 및 사용 방법
> 제품을 설치하기 위헤 필요한 소프트웨어 및 설치 방법을 작성하세요.
> 이 레포지토리를 git clone 하여 vscode 환경에서 실행한다.
> CUDA/ROCm을 활성화 해야한다.

> 제품을 설치하고 난 후, 실행 할 수 있는 방법을 작성하세요.

### 4. 소개 및 시연 영상
> 프로젝트에 대한 소개와 시연 영상을 넣으세요.

### 5. 팀 소개
> 팀원 소개 & 구성원 별 역할 분담 & 간단한 연락처를 작성하세요.
```

## 5. README.md 작성팁 
* 마크다운 언어를 이용해 README.md 파일을 작성할 때 참고할 수 있는 마크다운 언어 문법을 공유합니다.  
* 다양한 예제와 보다 자세한 문법은 [이 문서](https://www.markdownguide.org/basic-syntax/)를 참고하세요.

### 5.1. 헤더 Header
```
# This is a Header 1
## This is a Header 2
### This is a Header 3
#### This is a Header 4
##### This is a Header 5
###### This is a Header 6
####### This is a Header 7 은 지원되지 않습니다.
```
<br />

### 5.2. 인용문 BlockQuote
```
> This is a first blockqute.
>	> This is a second blockqute.
>	>	> This is a third blockqute.
```
> This is a first blockqute.
>	> This is a second blockqute.
>	>	> This is a third blockqute.
<br />

### 5.3. 목록 List
* **Ordered List**
```
1. first
2. second
3. third  
```
1. first
2. second
3. third
<br />

* **Unordered List**
```
* 하나
  * 둘

+ 하나
  + 둘

- 하나
  - 둘
```
* 하나
  * 둘

+ 하나
  + 둘

- 하나
  - 둘
<br />

### 5.4. 코드 CodeBlock
* 코드 블럭 이용 '``'
```
여러줄 주석 "```" 이용
"```
#include <stdio.h>
int main(void){
  printf("Hello world!");
  return 0;
}
```"

단어 주석 "`" 이용
"`Hello world`"

* 큰 따움표(") 없이 사용하세요.
``` 
<br />

### 5.5. 링크 Link
```
[Title](link)
[부산대학교 정보컴퓨터공학부](https://cse.pusan.ac.kr/cse/index..do)

<link>
<https://cse.pusan.ac.kr/cse/index..do>
``` 
[부산대학교 정보컴퓨터공학부](https://cse.pusan.ac.kr/cse/index..do)

<https://cse.pusan.ac.kr/cse/index..do>
<br />

### 5.6. 강조 Highlighting
```
*single asterisks*
_single underscores_
**double asterisks**
__double underscores__
~~cancelline~~
```
*single asterisks* <br />
_single underscores_ <br />
**double asterisks** <br />
__double underscores__ <br />
~~cancelline~~  <br />
<br />

### 5.7. 이미지 Image
```
<img src="image URL" width="600px" title="Title" alt="Alt text"></img>
![Alt text](image URL "Optional title")
```
- 웹에서 작성한다면 README.md 내용 안으로 이미지를 드래그 앤 드롭하면 이미지가 생성됩니다.
- 웹이 아닌 로컬에서 작성한다면, github issue에 이미지를 드래그 앤 드롭하여 image url 을 얻을 수 있습니다. (URL만 복사하고 issue는 제출 안 함.)
  <img src="https://github.com/user-attachments/assets/0fe3bff1-7a2b-4df3-b230-cac4ef5f6d0b" alt="이슈에 image 올림" width="600" />
  <img src="https://github.com/user-attachments/assets/251c6d42-b36b-4ad4-9cfa-fa2cc67a9a50" alt="image url 복사" width="600" />



### 5.8. 유튜브 영상 추가
```markdown
[![영상 이름](유튜브 영상 썸네일 URL)](유튜브 영상 URL)
[![부산대학교 정보컴퓨터공학부 소개](http://img.youtube.com/vi/zh_gQ_lmLqE/0.jpg)](https://www.youtube.com/watch?v=zh_gQ_lmLqE)    
```
[![부산대학교 정보컴퓨터공학부 소개](http://img.youtube.com/vi/zh_gQ_lmLqE/0.jpg)](https://www.youtube.com/watch?v=zh_gQ_lmLqE)    

- 이때 유튜브 영상 썸네일 URL은 유투브 영상 URL로부터 다음과 같이 얻을 수 있습니다.

- `Youtube URL`: https://www.youtube.com/watch?v={동영상 ID}
- `Youtube Thumbnail URL`: http://img.youtube.com/vi/{동영상 ID}/0.jpg 
- 예를 들어, https://www.youtube.com/watch?v=zh_gQ_lmLqE 라고 하면 썸네일의 주소는 http://img.youtube.com/vi/zh_gQ_lmLqE/0.jpg 이다.

