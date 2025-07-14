Django, Flask, FastAPI

1. Django
    철학: "Batteries included" – 모든 기능이 내장된 풀스택 프레임워크

    주요 특징:

    ORM, 인증, 관리자(admin) 페이지, 폼 처리 등 기본 내장

    프로젝트 구조가 정형화되어 있고, 관습 중심 (convention over configuration)

    대규모 웹서비스(예: 인스타그램) 개발에 적합

    장점:

    빠른 개발 가능 (많은 기능 내장)

    대형 커뮤니티 및 생태계

    안정적이고 오래된 레거시 시스템에도 적합

    단점:

    자유도가 낮고 유연성이 부족할 수 있음

    REST API 개발에는 약간의 설정 필요 (예: Django REST Framework 사용)

2. Flask
    철학: "Microframework" – 최소한의 기능만 제공, 확장은 사용자가 선택

    주요 특징:

    라우팅과 기본 서버 실행 기능만 제공

    ORM, 인증 등은 필요에 따라 라이브러리 설치 (ex. SQLAlchemy, Flask-Login)

    유연하고 단순한 구조, 빠른 프로토타이핑에 적합

    장점:

    학습 곡선이 낮음

    확장성 높고 자유도가 큼

    작은 프로젝트, 스타트업 서비스에 유리

    단점:

    규모가 커지면 관리 및 구조화가 어려울 수 있음

    비동기 지원이 부족하거나 복잡함

3. FastAPI
    철학: "Modern and fast" – 빠른 성능과 타입 기반 자동 문서화를 지향

    주요 특징:

    Python 타입 힌트를 적극 사용하여 Pydantic 기반의 데이터 검증 자동화

    OpenAPI (Swagger) 문서 자동 생성

    비동기(Async) 완전 지원 → 고성능 API 서버에 적합

    장점:

    매우 빠른 처리 속도 (Starlette 기반 비동기 지원)

    자동 문서화, 자동 검증으로 API 개발 생산성 ↑

    마이크로서비스, AI 백엔드 서버와 잘 어울림

    단점:

    전통적인 웹 템플릿 기반 서비스에는 부적합

    Django에 비해 커뮤니티 및 플러그인 생태계는 아직 작음