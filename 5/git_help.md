✅ 1. 작업 영역 생성 (Start a working area)
git clone: 기존 원격 저장소를 복제하여 새로운 디렉토리를 생성

git init: 현재 디렉토리를 새 Git 저장소로 초기화(또는 기존 저장소 재초기화)

✅ 2. 현재 변경 작업 (Work on the current change)
git add: 수정된 파일을 스테이징 영역(Index)에 추가

git mv: 파일/디렉토리/심볼릭 링크의 이름 변경 또는 이동

git restore: 수정된 파일을 마지막 커밋 상태로 되돌림

git rm: 파일을 작업 디렉토리 및 스테이징 영역에서 삭제

✅ 3. 히스토리 및 상태 확인 (Examine the history and state)
git bisect: 이진 탐색으로 버그를 발생시킨 커밋을 추적

git diff: 커밋 간 또는 작업 트리와의 변경점 비교

git grep: 저장소 내에서 특정 패턴 검색

git log: 커밋 기록 조회

git show: 특정 커밋, 태그, 객체 등의 상세 정보 출력

git status: 현재 작업 트리 상태 및 스테이징 상태 확인

✅ 4. 공통 히스토리 관리 (Grow, mark and tweak your common history)
git branch: 브랜치 생성, 목록 조회, 삭제

git commit: 스테이징된 변경 사항을 저장소에 기록

git merge: 다른 브랜치를 현재 브랜치에 병합

git rebase: 다른 브랜치 위로 커밋을 재배치(커밋 기록 정리 시 사용)

git reset: 현재 HEAD를 지정된 상태로 되돌림

git switch: 다른 브랜치로 전환

git tag: 특정 커밋에 태그 생성/목록 조회/삭제 (GPG 서명 가능)

✅ 5. 협업 (Collaborate)
git fetch: 원격 저장소에서 최신 커밋을 가져오되 병합하지 않음

git pull: fetch + merge (원격 저장소와 작업 브랜치를 동기화)

git push: 로컬 커밋을 원격 저장소에 업로드

