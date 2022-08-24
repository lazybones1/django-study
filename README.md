# django-study

# Django 설치

```markdown
python3 -m pip install django
```

# Django

```markdown
django-admin
```

- django의 관리 작업을 위한 커맨드 라인

```markdown
django-admin startproject 프로젝트이름 .
```

- 프로젝트 생성, ‘ . ‘ 은 현재 디렉토리를 의미

```markdown
python manage.py runserver 포트번호
```

- 서버 실행 (ctrl + c = 서버 실행 취소)
- 기본 포트 : 8080

```markdown
django-admin startapp 폴더이름
```

- app 생성 (폴더)

```markdown
urlpatterns = [
    path('', include('myapp.urls')),
]
```

- url 패턴 등록
- include 함수 → myapp.urls 파일을 가져옴 의미 → 해당 app폴더에 urls 생성
- ‘’ - 모든 경로로 들어왔을 경우 의미 → 원하는 url만 거를 수 있음

```python
// myapp - urls.py
urlpatterns = [
    path('', views.index),
    path('create/', views.create),
	  path('read/<id>', views.read),
]

// myapp - views.py
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('welcome')

def create(request):
    return HttpResponse('create')

def read(request, id):
    return HttpResponse('read' + id)
```

- url 매핑
- <> : 추가적인 변수 (pathvariable 같은 느낌)

## urls.py 정리

순서 : /read/1 → urls.py(myproject) → urls.py(myapp) → views.py(myapp) → def 함수 (views.py) → client

---

# CRUD

- ‘’’___‘’’ : 여러줄의 문자열 작성 가능
- global : 전역변수
- f’{변수 사용 가능}’

```python
request.POST['title']
```

- POST 요청으로 받은 데이터 확인
- 

## csrf 설정

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create(request):
	return
```

## redirect

```python
from django.shortcuts import redirect

@csrf_exempt
def create(request):
	return redirect('/')
```

# vscode extention 설치

- Python : 린트, 디버깅, 코드 탐색, 코드 서식 지정, 리팩터링, 변수 탐색기와 같은 기능등을 지원
- Python for VSCode : -> 구문 강조, 스니펫 및 린팅을 지원 (유지보수 지원 끊김)
- Python Extension Pack : vs code에서 인기많은 extension pack
- Python Type Hint : 입력 모듈 완성 및 type 힌트 자동 완성을 제공