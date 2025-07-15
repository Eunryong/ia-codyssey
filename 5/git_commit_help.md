✅ git commit 기본 개념
스테이징 영역(index)에 있는 변경 사항을 저장소에 커밋(commit)으로 기록합니다.

### 메시지 관련

-m <msg>
→ 커밋 메시지를 인라인으로 작성

-F <file> / --file <file>
→ 파일에 작성된 내용을 커밋 메시지로 사용

-C <commit>
→ 이전 커밋의 메시지를 그대로 재사용 (수정 X)

-c <commit>
→ 이전 커밋 메시지를 재사용하되, 편집 가능

### 수정/이전 커밋 관련

--amend
→ 직전 커밋 수정 (메시지나 스테이징된 파일 추가)

--fixup=<commit>
→ 특정 커밋을 수정하기 위한 "fixup" 커밋 생성 (이후 rebase --autosquash와 함께 사용)

--squash=<commit>
→ 특정 커밋과 합칠 "squash" 커밋 생성 (역시 rebase --autosquash와 함께 사용)

### 범위 및 대상

-a / --all
→ 수정된 모든 추적 중인(tracked) 파일을 자동으로 스테이징 후 커밋
(단, 새로운 파일은 포함되지 않음)

-i / --include
→ 특정 파일만 추가로 포함해 커밋

--only <file>
→ 지정한 파일만 커밋

### 서명 및 인증

-S / --gpg-sign[=<key-id>]
→ GPG 서명을 사용하여 커밋

### 메시지 편집기 동작

-e / --edit
→ 메시지 편집기를 강제로 열어 메시지 수정

--no-edit
→ 메시지 편집기 열지 않고 기존 메시지 그대로 사용 (예: --amend 시 자주 사용)

### 상태 및 설명 출력
-v / --verbose
→ 커밋 시 diff 내용을 메시지 편집기에 표시