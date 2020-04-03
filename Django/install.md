## django install

```
pip install django

django-admin startproject django_p829911

cd django_p829911
django-admin startapp board
```

## Django의 MVC (MTV)

## setting
settings.py 안에 추가된 app 써주기

## Migrations

migrations 폴더 안에 0001_inital.py 파일 생성
```
python3 manage.py makemigrations
```

app들이 사용하는 데이터베이스 자동 생성
db.sqlite3 생성
```
python3 manage.py migrate
```

db 확인
```
sqlite3 db.sqlite3

.tables
.schema fastcampus_fcuser
```

필드가 추가되면 makemigrations, migrate 다시

## 프로젝트 실행
```
python3 manage.py runserver
```
주소창 뒤에 /admin -> admin page

### admin 계정 생성
```
python3 manage.py createsuperuser
``` 

### Fcuser
model.py class에 아래 코드 추가
username 제대로 보이도록
```
    def __str__(self):
        return self.username 
```
