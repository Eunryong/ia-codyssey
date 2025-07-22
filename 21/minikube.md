# 📄 Minikube 클러스터 구조 및 설명

## 1. Minikube란 무엇인가?

-   **Minikube**는 로컬 환경(Windows/macOS/Linux)에서 **한 대의 노드로 구성된 Kubernetes 클러스터**를 빠르게 실행할 수 있게 해주는 툴입니다 ([Kubernetes][1], [GeeksforGeeks][2]).
-   주로 **개발, 학습, 테스트용**으로 사용되며, `minikube start` 한 번으로 클러스터를 부팅할 수 있습니다 ([Kubernetes][1]).

---

## 2. 클러스터 구성 요소

```text
┌──────────────────────────────────────┐
│         Minikube VM/환경            │
│                                      │
│  ┌──────────────┐   ┌─────────────┐  │
│  │ Control Plane│   │ Worker Node │  │
│  │ (Master)     │   │             │  │
│  │ - API Server │   │ - kubelet   │  │
│  │ - Controller │   │ - kube‑proxy│  │
│  │   Manager    │   │ - Container │  │
│  │ - Scheduler  │   └─────────────┘  │
│  │ - etcd       │                     │
│  └──────────────┘                     │
│                                      │
│  (단일 노드 안에 컨트롤 플레인과      │
│   워커 노드가 함께 실행되는 구조)     │
└──────────────────────────────────────┘
```

-   **Control Plane**:
    클러스터의 두뇌 역할. API 서버, 컨트롤러 매니저, 스케줄러, etcd 등을 포함 ([Mirantis][3]).
-   **Worker Node**:
    실제 애플리케이션이 동작하는 노드. kubelet, kube-proxy, 컨테이너 런타임, 그리고 Pod 등을 포함 ([fusionauth.io][4]).

---

## 3. Minikube의 특징

-   **단일 노드 클러스터**:
    실험/테스트 목적의 로컬 환경에 적합 ([GeeksforGeeks][2], [Kubernetes][1]).
-   **간단한 설치와 관리**:
    Docker 기반 드라이버 등으로 설치 후 CLI(`minikube start/stop/delete`)로 쉽게 제어 ([docs.bitnami.com][5], [Kubecademy][6]).
-   **쿠버네티스 핵심 기능 포함**:
    Pod, Deployment, Service 등 대부분 리소스를 지원하지만, LoadBalancer 타입은 클라우드 환경이 아니면 유사하게 작동 ([Kubernetes][7]).

---

## 4. 용도 및 장점

-   **로컬 개발/디버깅**: 실제 클러스터가 필요한 워크플로우를 로컬에서 손쉽게 실습 가능.
-   **교육 환경**: 쿠버네티스 개념 학습시 설치 부담 없이 활용.
-   **CI/CD 테스트**: 파이프라인 중단 없이 자동화 테스트용 클러스터로 활용.

---

## 5. 공식문서 vs 비공식자료 비교

-   **공식 Kubernetes 홈페이지**에서는 Minikube 관련 개략적인 설명과 시작 가이드를 제공하며, 전체 쿠버네티스 클러스터 구조는 이미 포함되어 있음 ([Kubernetes][1], [Kubernetes][7]).
-   **Minikube 전용 아키텍처 그림**은 공식 사이트보다는 블로그, 기술문서, 커뮤니티 글 등에서 많이 사용됨 .

minikube start
minikube start --driver=docker
minikube delete
