## Pod와 Service의 역할

## Pod

Kubernetes에서 배포 가능한 가장 작은 단위

1개 이상의 컨테이너와 스토리지, 네트워크 구성을 포함

동일 Pod 내 컨테이너는 동일 네트워크 네임스페이스 공유

## Service

Pod 집합을 추상화하여 네트워크 접근을 가능하게 함

Pod의 IP는 변할 수 있지만 Service의 IP는 고정되어 안정적인 통신 가능

주요 타입:

ClusterIP: 클러스터 내부에서만 접근

NodePort: 클러스터 외부에서도 노드의 IP + 지정된 포트로 접근

LoadBalancer: 클라우드 환경에서 외부 로드밸런싱 지원
