## 1.0.0

-   가채점기 배포 시작

### 1.0.1

-   버그 수정
-   실행 방법 변경 (향후 기능 확장 고려)

| 변경 후 | `python -m boj judge source_file` |
| ---- | --------------------------------- |
| 변경 전 | `python -m boj source_file`       |

### 1.0.2

-   버그 수정
-   모듈 구조 변경 (리팩토링)
-   실행 방법 추가 : `python -m boj.judge source_file`

* * *

## 1.1.0

-   문제 폴더 구성기 추가

### 1.1.1

-   `config.ini`의 UTF-8 인코딩 관련 문제 해결
-   버전 업데이트 시, `config.ini`도 업데이트 하도록 기능구현
-   향후 간편한 사용자 설정을 지원하기 위해 `boj.config` 모듈 개편
-   `boj.__version__` 변수 추가
-   출력 문구 중 어색한 표현 수정

### 1.1.2

-   C++ 언어 실행이 되지 않는 문제 수정

### 1.1.3

-   시간 초과시 출력되던 잘못된 수행시간을 더 이상 출력하지 않음

### 1.1.4

-   C언어 지원 (gcc 컴파일러 이용)

### 1.1.5

-   문제 저장소 구성 후 (git commit / dummy 파일 생성) 기능 추가