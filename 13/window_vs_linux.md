## 동작 원리 비교

| 구분              | **리눅스 컨테이너 (기본)**                                                    | **윈도우 컨테이너**                                                                                       |
| ----------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **기반 커널**     | **리눅스 커널**                                                               | **윈도우 NT 커널**                                                                                        |
| **실행 방식**     | WSL2(Windows Subsystem for Linux 2) 또는 Hyper-V 기반 경량 VM 위에서 실행     | Windows Server 컨테이너 또는 Hyper-V 격리 모드로 실행                                                     |
| **이미지 호환성** | Docker Hub의 대부분의 공식 이미지 사용 가능 (예: `python`, `nginx`, `ubuntu`) | Windows 전용 이미지 사용 (`mcr.microsoft.com/windows/nanoserver`, `mcr.microsoft.com/windows/servercore`) |
| **파일 시스템**   | Linux 기반 파일 시스템 (ext4)                                                 | Windows NTFS 기반 파일 시스템                                                                             |
| **네트워크**      | 가상화된 Linux 네트워크 스택 사용                                             | Windows 네트워크 스택 사용                                                                                |
| **성능**          | WSL2 기반으로 거의 리눅스 네이티브에 가까운 성능                              | Hyper-V 격리 모드 사용 시 상대적으로 느림                                                                 |
| **주 사용 사례**  | 대부분의 오픈소스 및 클라우드 네이티브 애플리케이션 실행                      | .NET Framework, Windows Server 기반 레거시 앱 실행                                                        |

## 이미지 및 호환성

🔹 리눅스 컨테이너
이미지 수: Docker Hub에 공개된 대부분의 이미지 사용 가능

예시: python:3.11, node:18, nginx:latest, ubuntu:20.04

🔹 윈도우 컨테이너
이미지 제한: Windows 전용 이미지만 사용 가능
(리눅스용 이미지와 상호 호환되지 않음)

예시:

mcr.microsoft.com/windows/nanoserver

mcr.microsoft.com/windows/servercore

## 운영 및 전환

-   컨테이너 전환 방법
    Docker Desktop의 트레이 메뉴에서 "Switch to Windows containers..." 또는 **"Switch to Linux containers..."**로 전환

두 환경은 동시에 실행할 수 없음 (하나만 활성화 가능)

-   Dockerfile 호환성
    리눅스용 Dockerfile과 윈도우용 Dockerfile은 명령어와 기반 이미지가 다르며, 서로 호환되지 않음.

## 사용 목적 정리

| 목적                                         | 권장 컨테이너      |
| -------------------------------------------- | ------------------ |
| **일반 웹 서비스, 오픈소스 소프트웨어 배포** | ✅ 리눅스 컨테이너 |
| **AI/ML, 데이터베이스, 마이크로서비스**      | ✅ 리눅스 컨테이너 |
| **레거시 .NET Framework 앱 실행**            | ✅ 윈도우 컨테이너 |
| **Windows Server 기반 서비스 테스트**        | ✅ 윈도우 컨테이너 |

## 요약

리눅스 컨테이너: Docker Desktop의 기본, 이미지 호환성 및 성능 우수 → 대부분의 경우 권장

윈도우 컨테이너: Windows 전용 레거시 애플리케이션에 한정, 이미지와 사용 사례가 제한적

## 추가 안내 가능

두 컨테이너 간 이미지 전환 불가 이유

Windows 컨테이너의 Hyper-V 격리 vs 프로세스 격리 차이

리눅스 컨테이너 + WSL2 성능 최적화 방법
