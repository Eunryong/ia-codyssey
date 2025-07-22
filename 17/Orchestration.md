## 1. 컨테이너 오케스트레이션의 정의 📦

컨테이너 오케스트레이션(Container Orchestration)은 다수의 컨테이너화된 애플리케이션을 **자동으로 배포, 스케일링, 네트워킹, 로드 밸런싱, 복구** 등을 관리하는 프로세스로, 인프라 및 애플리케이션 운영을 자동화하고 안정적으로 유지하는 기술입니다.

쿠버네티스 공식 개요에 따르면:

> Kubernetes는 컨테이너화된 작업 부하와 서비스를 관리하기 위한 **이식성(portable)** 있고 **확장성(extensible)** 있는 **오픈소스 플랫폼**으로, **선언적 구성(declarative configuration)** 및 **자동화**를 지원합니다 ([infosys.com][1], [Kubernetes][2]).

즉, 컨테이너 환경을 코드화하여 시스템이 자동으로 상태를 유지하도록 해주는 기술입니다.

---

## 2. Kubernetes 아키텍처 그림 및 설명 🏗

```
           ┌──────────────────────────┐
           │       Control Plane      │
           │                          │
           │  ┌──────────┐   ┌──────┐ │
           │  │ kube-apiserver       │
           │  │ kube-scheduler       │
           │  │ kube-controller-mgr  │
           │  │     etcd             │
           │  └──────────┴─────────┬┘
           └────────────────────────┘
                        │
            ┌───────────┴────────────┐
            │   Worker Node(s)       │
            │ ┌────────────────────┐ │
            │ │ kubelet            │ │
            │ │ kube-proxy         │ │
            │ │ container runtime  │ │
            │ │ (e.g., containerd) │ │
            │ └────────────────────┘ │
            └────────────────────────┘
```

-   **Control Plane (제어 평면)**

    -   `kube-apiserver`: 모든 API 요청의 진입점
    -   `etcd`: 클러스터 구성 상태를 저장하는 분산 KV 저장소
    -   `kube-scheduler`: 노드 리소스 기반으로 Pod 배치 결정
    -   `kube-controller-manager`: 복제, 노드, 종료 처리 등 다양한 컨트롤러 동작 ([위키백과][3], [Kubernetes][4])

-   **Worker Node (작업 노드)**

    -   `kubelet`: 노드 상태를 제어 평면과 동기화하며 Pod 실행
    -   `kube-proxy`: 네트워킹·서비스 추상화 및 로드 밸런싱
    -   `container runtime`: 컨테이너 실행 엔진 (CRI 표준, 예: containerd) ([Kubernetes][4], [위키백과][3])

이 구조는 **‘제어 평면 ↔ 작업 노드’**로 나뉘며, 중앙 API 기반 관리 계층과 실제 실행 계층이 연결된 형태입니다.

---

## 3. CNCF Landscape를 참고한 과제

### A. 컨테이너 오케스트레이션 종류 3가지

CNCF Landscape에서 ‘Orchestration & Management’ 분야의 대표 툴 중:

1. **Kubernetes** – 오픈소스 컨테이너 관리 시스템 ([위키백과][3], [loft.sh][5])
2. **Apache Mesos** – 대규모 분산 시스템을 위한 컨테이너 및 작업 스케줄러 (참고 Landscape)
3. **HashiCorp Nomad** – 다중 워크로드 스케줄링 및 오케스트레이션 툴

4. KEDA (graduated)
   Kubernetes Event-driven Autoscaling

개요:
쿠버네티스 클러스터에서 워크로드(주로 파드, 특히 서버리스/백그라운드 작업 등)를 이벤트 기반으로 자동 스케일링해주는 오픈소스 컴포넌트입니다.

특징:

HTTP 요청, 메시지 큐(예: Kafka, RabbitMQ, Azure Queue), 데이터베이스 등 다양한 이벤트 소스를 기준으로 파드 수를 조절

기존 HPA(Horizontal Pod Autoscaler)는 CPU/메모리 사용량만으로 스케일링,
KEDA는 이벤트 기반(큐 길이, 메시지 수 등)으로 스케일링

graduated: CNCF에서 ‘성숙한 프로젝트’로 인정(안정적, 실전 적용 충분)

주요 사용 예시:
메시지 큐에 쌓인 메시지가 많아지면 파드를 더 늘리고, 줄어들면 자동 축소

2. Kubernetes (graduated)
   컨테이너 오케스트레이션의 표준

개요:
컨테이너화된 애플리케이션의 배포, 관리, 스케일링, 네트워킹, 장애 복구 등 전체 라이프사이클을 자동화하는 오픈소스 플랫폼

특징:

컨테이너의 표준 관리 솔루션 (구글이 개발, CNCF에서 관리)

파드, 서비스, 디플로이먼트, 네임스페이스 등 다양한 리소스를 선언적으로 관리

멀티 클라우드, 하이브리드, 온프레미스 등 어디서든 실행 가능

graduated: CNCF에서 완전히 검증된 대표적인 졸업(Graduated) 프로젝트

주요 사용 예시:
대규모 서비스, 마이크로서비스 아키텍처, 데브옵스 자동화, 멀티 클러스터 운영 등

3. Crossplane (incubating)
   쿠버네이티브 클라우드 리소스 프로비저닝

개요:
쿠버네티스 API를 이용해 AWS, Azure, GCP 등 클라우드 인프라 자원을 코드로 관리하고, 프로비저닝 및 라이프사이클을 통합할 수 있게 해주는 오픈소스 프로젝트입니다.

특징:

쿠버네티스 CRD(Custom Resource Definition) 기반으로 인프라(서버, 데이터베이스, 스토리지 등)를 직접 선언/관리

Terraform처럼 인프라를 코드로 다루지만, 쿠버네티스 API와 통합되어 DevOps 및 GitOps에 강점

incubating: CNCF의 ‘인큐베이팅’ 단계(활발히 개발 중, 성숙기 직전)

주요 사용 예시:
쿠버네티스 YAML로 AWS RDS, S3, Azure VM, Google Cloud Storage 등 프로비저닝 및 관리 자동화

> CNCF Landscape 범주 내 오케스트레이션 툴은 크게 Kubernetes 외에 Nomad, Mesos 등 다양한 옵션이 포함되어 있습니다 ([Kubernetes][6], [Aqua][7]).

### B. Kubernetes 배포판 3가지 및 사용 목적

CNCF Landscape의 `Certified Kubernetes - Distribution` 항목에서 선택:

1. **k0s**

    - 단일 바이너리, 경량화된 클러스터 구성
    - 로컬 테스트나 IoT, 엣지 환경에 적합 ([landscape.cncf.io][8])

2. **Red Hat OpenShift**

    - 기업용 기능(빌트인 CI/CD, 보안, 멀티테넌시 포함) 제공
    - 엔터프라이즈 환경에 널리 사용 (Landscape 언급) ([위키백과][9])

3. **Rancher Kubernetes (RKE)**

    - 멀티클러스터 관리, UI 및 사용자 관리 기능 포함
    - 다양한 인프라(온프레/클라우드) 환경을 관리하는 데 최적

이들 배포판은 각기 **경량화·개발용(k0s)**, **기업/보안 중심(OpenShift)**, \*\*멀티클러스터 및 관리 중심(RKE)\*\*으로 구분됩니다.

---

### 📌 과제 요약

| 항목                             | 내용                                                                  |
| -------------------------------- | --------------------------------------------------------------------- |
| **컨테이너 오케스트레이션 정의** | 컨테이너화된 애플리케이션을 자동 배포·스케일·관리하는 기술            |
| **Kubernetes 아키텍처**          | Control Plane (API 서브시스템) + Worker Node 구조                     |
| **오케스트레이션 툴 3종**        | Kubernetes, Nomad, Mesos                                              |
| **배포판 3종 & 용도**            | k0s (경량/엣지), OpenShift (엔터프라이즈), Rancher RKE (멀티클러스터) |
