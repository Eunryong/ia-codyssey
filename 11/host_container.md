## 개념 비교
| 구분        | 호스트 포트 (Host Port)                                   | 컨테이너 포트 (Container Port)               |
| --------- | ---------------------------------------------------- | -------------------------------------- |
| **정의**    | 도커가 실행되는 **호스트 운영체제(PC/서버)**에서 외부와 통신할 때 사용하는 포트 | **컨테이너 내부** 애플리케이션이 통신에 사용하는 포트        |
| **역할**    | 외부 사용자(브라우저, API 클라이언트 등)가 접속할 때 연결되는 진입점            | 컨테이너 내부 애플리케이션이 서비스하는 포트 (예: 웹서버 80포트) |
| **접근 주체** | **외부(호스트 OS 밖)**에서 접근                            | **컨테이너 내부**에서만 접근                      |
| **설정 방법** | `docker run` 시 `-p <호스트포트>:<컨테이너포트>`로 매핑             | 애플리케이션 설정 파일 또는 컨테이너 이미지 내부에서 고정       |


## 동작 원리
사용자는 호스트 포트를 통해 접속한다.

Docker가 네트워크 브릿지를 이용해 호스트 포트 → 컨테이너 포트로 요청을 전달한다.

컨테이너 내부에서 애플리케이션이 컨테이너 포트로 요청을 처리한다.

[외부 접속자] → (호스트 포트) → [Docker 네트워크] → (컨테이너 포트) → [애플리케이션]

## 정리
호스트 포트 = 외부에서 접근하는 관문

컨테이너 포트 = 내부 애플리케이션의 서비스 포트

포트 매핑이 없다면 외부에서 컨테이너에 직접 접근할 수 없음