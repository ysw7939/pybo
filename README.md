# 커밋 컨밴션


<유형>(<범위>): <메시지>

유형:
- feat: 새로운 기능 추가
- fix: 버그 수정
- docs: 문서 변경
- style: 코드 스타일 변경 (공백, 포맷팅 등)
- refactor: 코드 리팩토링
- test: 테스트 코드 추가 또는 수정
- chore: 빌드 프로세스 또는 보조 도구의 변경

범위 (옵션):
- 변경된 파일, 모듈 또는 기능 등을 명시

메시지:
- 명령형 어조를 사용하여 간결하게 작성
- 첫 번째 줄에는 간단하게 요약
- 두 번째 줄은 비어두고, 세 번째 줄부터 자세한 내용 작성 (선택)

예시:
```
feat(user-auth): add user authentication feature
fix(bug-report): resolve issue with login button
docs(readme): update installation instructions
style(css): format code according to style guide
refactor(api): improve error handling in API calls
test(login): add unit tests for login functionality
chore(build): update dependencies in build process
```

```
pybo
├─ common
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     └─ __init__.cpython-312.pyc
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ admin.cpython-312.pyc
│     ├─ apps.cpython-312.pyc
│     ├─ forms.cpython-312.pyc
│     ├─ models.cpython-312.pyc
│     ├─ urls.cpython-312.pyc
│     ├─ views.cpython-312.pyc
│     └─ __init__.cpython-312.pyc
├─ config
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ settings.cpython-312.pyc
│     ├─ urls.cpython-312.pyc
│     ├─ wsgi.cpython-312.pyc
│     └─ __init__.cpython-312.pyc
├─ db.sqlite3
├─ fileupload
│  ├─ media
│  ├─ migrations
│  │  └─ __pycache__
│  ├─ templates
│  └─ __pycache__
├─ manage.py
├─ media
├─ pybo
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_rename_create_data_question_create_date.py
│  │  ├─ 0003_question_author.py
│  │  ├─ 0004_answer_author.py
│  │  ├─ 0005_answer_modify_date_question_modify_date.py
│  │  ├─ 0006_answer_voter_question_voter_alter_answer_author_and_more.py
│  │  ├─ 0007_question_imgfile.py
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     ├─ 0001_initial.cpython-312.pyc
│  │     ├─ 0002_rename_create_data_question_create_date.cpython-312.pyc
│  │     ├─ 0003_question_author.cpython-312.pyc
│  │     ├─ 0004_answer_author.cpython-312.pyc
│  │     ├─ 0005_answer_modify_date_question_modify_date.cpython-312.pyc
│  │     ├─ 0006_answer_voter_question_voter_alter_answer_author_and_more.cpython-312.pyc
│  │     ├─ 0007_question_imgfile.cpython-312.pyc
│  │     └─ __init__.cpython-312.pyc
│  ├─ models.py
│  ├─ templatetags
│  │  ├─ pybo_filter.py
│  │  └─ __pycache__
│  │     └─ pybo_filter.cpython-312.pyc
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views
│  │  ├─ answer_views.py
│  │  ├─ base_views.py
│  │  ├─ question_views.py
│  │  └─ __pycache__
│  │     ├─ answer_views.cpython-312.pyc
│  │     ├─ base_views.cpython-312.pyc
│  │     ├─ question_views.cpython-312.pyc
│  │     └─ __init__.cpython-312.pyc
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ admin.cpython-312.pyc
│     ├─ apps.cpython-312.pyc
│     ├─ forms.cpython-312.pyc
│     ├─ models.cpython-312.pyc
│     ├─ urls.cpython-312.pyc
│     ├─ views.cpython-312.pyc
│     └─ __init__.cpython-312.pyc
├─ README.md
├─ static
│  ├─ 1700733379816_1700733430057.jpg
│  ├─ 1701172004687_1701173324402.jpg
│  ├─ bg1.png
│  ├─ bg1_ZXH0RUg.png
│  ├─ bootstrap.min.css
│  ├─ bootstrap.min.js
│  ├─ bug.png
│  ├─ IMG_2775_1701339689792.jpeg
│  ├─ q1.jpg
│  ├─ seolyoon.jpg
│  ├─ style.css
│  ├─ 고양이.jpg
│  ├─ 고양이_w97DsCj.jpg
│  ├─ 빈대.png
│  └─ 파비콘.png
└─ templates
   ├─ base.html
   ├─ common
   │  ├─ login.html
   │  └─ signup.html
   ├─ form_errors.html
   ├─ navbar.html
   └─ pybo
      ├─ answer_form.html
      ├─ question_detail.html
      ├─ question_form.html
      └─ question_list.html

```