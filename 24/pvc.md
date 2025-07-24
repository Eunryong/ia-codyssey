
# **Kubernetes Storage 관련 문서**

## 1. **AccessMode의 종류와 특징**

| AccessMode                      | 약어   | 특징                                                                | 사용 사례                                           |
| ------------------------------- | ---- | ----------------------------------------------------------------- | ----------------------------------------------- |
| **ReadWriteOnce**               | RWO  | 단일 노드에서 **읽기/쓰기** 가능. 여러 Pod가 같은 노드에서 공유 가능하지만, **다른 노드에서 접근 불가** | MySQL, WordPress, Redis 등 단일 노드 기반 DB           |
| **ReadOnlyMany**                | ROX  | 여러 노드에서 **읽기 전용**으로 접근 가능. **쓰기 불가**                              | 컨텐츠 배포, 정적 파일 공유                                |
| **ReadWriteMany**               | RWX  | 여러 노드에서 동시에 **읽기/쓰기** 가능                                          | NFS, GlusterFS, CephFS 등 다중 Pod가 동시에 공유해야 하는 환경 |
| **ReadWriteOncePod** *(v1.22+)* | RWOP | 단일 Pod만 읽기/쓰기 가능. 다른 Pod는 접근 불가                                   | 보안이 중요한 단일 Pod 애플리케이션                           |

---

## 2. **PVC와 PV의 역할**

### **(1) PersistentVolume (PV)**

* **정의**: 클러스터 관리자가 생성하는 스토리지 자원으로, **스토리지의 실제 물리적 공간**을 추상화한 리소스.
* **특징**:

  * 클러스터의 자원이며 Pod와 독립적.
  * NFS, AWS EBS, GCE PD, Ceph, HostPath 등 다양한 스토리지 백엔드를 지원.
  * **수명 주기**: Pod와 독립적 (Pod가 삭제되어도 PV는 유지 가능).

### **(2) PersistentVolumeClaim (PVC)**

* **정의**: 사용자가 스토리지를 요청하는 선언적 사양(Claim).
* **특징**:

  * Pod가 필요한 스토리지 크기와 AccessMode를 PVC로 요청.
  * PVC가 PV와 바인딩되면 Pod에서 volume으로 마운트 가능.

### **(3) 관계**

* 사용자가 PVC를 생성하면, 쿠버네티스는 **PVC 조건과 일치하는 PV를 자동 바인딩**.
* PVC가 삭제되면 **PV의 Reclaim Policy**에 따라 동작이 결정됨:

  * **Retain**: PV를 유지
  * **Recycle**: 데이터 삭제 후 PV 재사용
  * **Delete**: PV와 실제 스토리지 삭제

---

## 3. **PV의 볼륨 타입과 특징**

| 볼륨 타입                                 | 특징                                     | 사용 사례                 |
| ------------------------------------- | -------------------------------------- | --------------------- |
| **hostPath**                          | 노드의 로컬 디렉토리를 Pod에 마운트                  | 개발, 테스트 환경 전용         |
| **nfs**                               | NFS(Network File System) 서버 사용. RWX 지원 | 다중 Pod 공유 스토리지        |
| **awsElasticBlockStore**              | AWS EBS 사용. RWO 지원                     | AWS 기반 프로덕션 환경        |
| **gcePersistentDisk**                 | GCP의 Persistent Disk 사용. RWO 지원        | GCP 기반 서비스            |
| **azureDisk / azureFile**             | Azure 클라우드 스토리지. azureFile은 RWX 지원     | Azure 기반 서비스          |
| **cephfs**                            | Ceph 파일 시스템. RWX 지원                    | 대규모 공유 스토리지           |
| **glusterfs**                         | GlusterFS 네트워크 파일 시스템                  | RWX, 고가용성 필요 환경       |
| **csi (Container Storage Interface)** | 다양한 스토리지 벤더 통합 인터페이스                   | 최신 Kubernetes 스토리지 표준 |
| **local**                             | 노드 로컬 디스크를 PV로 사용                      | 성능이 중요한 워크로드(예: DB)   |
| **emptyDir** *(참고)*                   | Pod가 삭제되면 데이터도 삭제됨(영구 저장 아님)           | 캐시, 임시 데이터 저장용        |

---

## **결론 및 요약**

1. **AccessMode**

   * 기본적으로 `ReadWriteOnce(RWO)`가 가장 많이 사용되며, **RWX는 네트워크 파일 시스템 필요**.

2. **PVC와 PV**

   * **PVC**: 사용자 스토리지 요청
   * **PV**: 실제 스토리지 자원 (관리자가 생성하거나 StorageClass로 동적 생성)

3. **PV 볼륨 타입**

   * **클라우드**: AWS EBS, GCE PD, Azure Disk
   * **온프레미스/공유**: NFS, CephFS, GlusterFS
   * **테스트용**: hostPath

