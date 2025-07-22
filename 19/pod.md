## YAML 형태로 출력한 Pod 정보의 구조

파일: david-info.txt 분석 (주요 구조)

(1) apiVersion & kind
apiVersion: v1 → Kubernetes API 버전

kind: Pod → 리소스 종류(Pod)

(2) metadata
Pod의 기본 정보(이름, 라벨, 네임스페이스 등)

예:

name: david-pod

labels: app: david

namespace: default

(3) spec
Pod의 스펙 및 실행 설정

주요 항목:

containers: 컨테이너 이미지와 설정

image: eunryong/david:v1.0

name: david-pod

ports, volumeMounts 등

restartPolicy: Always → Pod 재시작 정책

nodeName: docker-desktop → 실행 중인 노드

(4) status
Pod의 현재 상태

주요 항목:

phase: Running → 현재 실행 상태

podIP: 10.1.0.29 → Pod 내부 IP

containerStatuses: 컨테이너 실행 상태, 재시작 횟수 등
