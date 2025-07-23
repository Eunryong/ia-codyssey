## ReplicaSet의 역할

정의
ReplicaSet은 특정 수의 Pod 복제본(replicas)을 항상 유지하는 역할을 담당하는 Kubernetes 리소스입니다.

주요 기능
Pod 수 보장:
지정된 replicas 개수를 유지하며, Pod가 죽으면 새로 생성.

간단한 Pod 관리:
단일 애플리케이션의 고가용성을 위해 사용.

레이블 기반 Pod 관리:
selector로 특정 라벨을 가진 Pod만 관리.

한계
ReplicaSet 자체는 애플리케이션 업데이트(롤링 업데이트, 롤백 등)를 지원하지 않음

주로 Deployment에 의해 자동으로 생성 및 관리됨.

## Deployment의 역할

정의
Deployment는 Pod와 ReplicaSet의 상위 관리 리소스로, 애플리케이션의 배포, 업데이트, 롤백 등을 자동화합니다.

주요 기능
롤링 업데이트

Pod를 순차적으로 새 버전으로 교체하여 무중단 배포 가능.

롤백 지원

문제가 발생하면 이전 버전으로 빠르게 복귀 가능.

ReplicaSet 관리 자동화

Deployment가 내부적으로 ReplicaSet을 생성하고, Pod 수 유지와 업데이트를 관리.

선언적 상태 관리

사용자가 정의한 "원하는 상태(Desired State)"를 지속적으로 유지.

## 관계

| 구분          | Deployment                                            | ReplicaSet                         |
| ------------- | ----------------------------------------------------- | ---------------------------------- |
| **역할**      | Pod와 ReplicaSet을 통합 관리, 배포 및 업데이트 자동화 | 지정된 Pod 복제본 수 유지          |
| **사용 주체** | 사용자가 직접 생성                                    | 보통 Deployment가 자동 생성        |
| **업데이트**  | 롤링 업데이트, 롤백 지원                              | 단순 복제본 유지(업데이트 지원 X)  |
| **생성 명령** | `kubectl apply -f deployment.yaml`                    | `kubectl apply -f replicaset.yaml` |

```
Deployment  (배포, 업데이트, 롤백 관리)
 └── ReplicaSet  (Pod 복제본 수 유지)
      └── Pod (N개)
```

## Deployment를 사용하는 이유

| 이유                       | 설명                                                                                    |
| -------------------------- | --------------------------------------------------------------------------------------- |
| **Deployment가 상위 호환** | ReplicaSet의 모든 기능(복제본 유지)을 포함하면서 롤링 업데이트, 롤백까지 지원           |
| **관리 자동화**            | Deployment가 새 버전 배포 시 자동으로 새로운 ReplicaSet을 생성하고 이전 ReplicaSet 정리 |
| **운영 표준**              | Kubernetes 공식 권장 방식은 **Deployment 사용 → ReplicaSet 자동 관리**                  |
