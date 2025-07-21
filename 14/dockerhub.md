## DockerHub를 사용하는 이유

공식 이미지 제공

DockerHub는 Docker에서 공식적으로 관리하는 다양한 **공식 이미지(Official Image)**를 제공하므로, 안정성과 신뢰성이 높습니다.

예: ubuntu, nginx, mysql 등 검증된 이미지 사용 가능

전 세계적인 표준 레지스트리

전 세계적으로 가장 많이 사용되는 컨테이너 이미지 레지스트리로, 커뮤니티와의 호환성이 높습니다.

손쉬운 이미지 배포 및 공유

자신이 만든 Docker 이미지를 쉽게 push하여 다른 사용자와 공유할 수 있습니다.

docker push와 docker pull 명령으로 간단히 업로드·다운로드 가능

CI/CD와의 연동 용이

GitHub Actions, Jenkins, GitLab CI/CD 등 다양한 자동화 툴과 연동이 용이해 DevOps 환경에 적합합니다.

무료 및 유료 플랜 지원

무료 플랜으로도 개인 프로젝트에 충분히 사용 가능하며, 유료 플랜을 통해 비공개 저장소와 팀 단위 협업도 지원합니다.

## Container Registry 종류 3가지

DockerHub

가장 널리 사용되는 Docker 공식 레지스트리

공개 및 비공개 저장소 지원

URL: https://hub.docker.com

GitHub Container Registry (GHCR)

GitHub과 통합된 컨테이너 레지스트리

코드와 컨테이너 이미지를 동일한 GitHub 저장소에서 관리 가능

URL: https://ghcr.io

Amazon Elastic Container Registry (ECR)

AWS에서 제공하는 관리형 레지스트리

IAM 기반 보안과 AWS 서비스 통합에 강점

대규모 프로덕션 환경에서 사용 적합

URL: https://aws.amazon.com/ecr/
