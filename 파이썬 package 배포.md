# 파이썬 package 배포 하기

### setup.py 설정

`setup.py` 파일을 프로젝트의 root 디렉토리에 생성한다. 대부분의 빌드 설정을 `setup.py` 를 통해서 한다. `setup.py` 파일을 통해 할 수 있는 설정들은 여러가지가 있는데 그 중 가장 자주 쓰이는 설정들은 아래와 같다.

- **name**: 프로젝트 이름
- **version**: 배포 버전
- **description**: 프로젝트 설명
- **author**: 프로젝트 저자
- **author_email**: 저자의 이메일
- **url**: 프로젝트 사이트 주소. 오픈소스의 경우 대부분 깃헙 주소를 사용한다.
- **download_url**: 해당 라이브러리의 실행 바이너리 다운 받는 주소. 마찬가지로 오픈소스의 경우 대부분 깃헙의 archive 주소를 설정한다.
- **install_requires**: 해당 라이브러리를 사용하기 위해서 인스톨 되야하는 dependency package, 해당 라이브러리를 `pip` 를 통해 인스톨 할 때 이곳에 나열된 라이브러리들을 같이 인스톨한다.
- **packages**: 빌드에 포함될 package들. 한 프로젝트에 여러 package가 있을수도 있고 또한 빌드에서 제외할 package들 (예를 들어 test 코드나 doc)이 있을 수 있으므로 그러한 설정을 한다. 대부분 `setuptools.find_packages` 함수를 사용하여 자동으로 포함될 package들을 찾게 하고 대신에 제외되어야 할 package 들을 `exclude` 인자를 통해 설정해준다.
- **keywords**: 해당 프로젝트 관련 키워드
- **python_requires**: 서포트 하는 파이썬 버전 설정
  - Python 3.6 에서만 실행된다면: `=3.6`
  - Python 3 버전 이상에서는 다 실행된다면: `>=3`
- **package_data**: 기본적으로 `setup` 은 파이썬 파일만 빌드에 포함시킨다. 파이썬 파일이 아닌 외부 파일을 포함시키기 위해선 포함시키고자 하는 파일들을 이 옵션에 명시해 줘야 포함된다. 그렇지 않으면 포함이 되지 않는다. 이 옵션 설정을 해주지 않거나 잘못 설정해주어서 문제가 생기는 경우가 있으므로 주의해야 한다.
- **zip_safe**: 위의 `package_data` 설정을 하였으면 `zip_safe` 설정도 해주어야 하며 `False` 로 설정해 주어야 한다.
- **classifiers**: PYPI에 등록될 메타 데이터 설정이다. 예를 들어 서포트 하는 python 버전 정보를 명시할 수 있다. 하지만 이건 PYPI에 등록될 메타 데이터일 뿐이고 실제 빌드에는 영향을 주지 않는다.

```python
from setuptools import setup, find_packages

setup(
    name             = 'pyquibase',
    version          = '1.0',
    description      = 'Python wrapper for liquibase',
    author           = 'Eun Woo Song',
    author_email     = 'songew@gmail.com',
    url              = 'https://github.com/rampart81/pyquibase',
    download_url     = 'https://githur.com/rampart81/pyquibase/archive/1.0.tar.gz',
    install_requires = [ ],
    packages         = find_packages(exclude = ['docs', 'tests*']),
    keywords         = ['liquibase', 'db migration'],
    python_requires  = '>=3',
    package_data     =  {
        'pyquibase' : [
            'db-connectors/sqlite-jdbc-3.18.0.jar',
            'db-connectors/mysql-connector-java-5.1.42-bin.jar',
            'liquibase/liquibase.jar'
    ]},
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
```

`setuptools` 를 사용해 `setup` 설정을 해줬기 때문에 아직 `setuptools` 가 인스톨 되어 있지 않다면 인스톨 한다.

```bash
pip install setuptools
```



### Setup.cfg

만일 README 파일이 마크다운 형태로 되어 있다면 `setup.cfg` 파일을 아래와 같이 설정 해준다.

```
[metadata]
description-file = README.md
```



### 빌드하기

빌드 하는 방법은 몇가지가 있지만 공식적으로는 `wheel` 을 사용하여 빌드하는 것이 권장된다. `wheel` 은 build package인데 일반적인 source distribution보다 더 빨리 인스톨 되기에 공식적으로 권장 된다. 아래 커맨드를 실행하여 `wheel` 을 인스톨하고 빌드를 하도록 한다.

```bash
pip install wheel
python setup.py bdist_wheel
```

위의 커맨드를 실행하면 `dist` 폴더가 생기고 그 안에 빌드 파일이 생성된다.



### 배포하기

배포는 `twine`으ㄹ 사용하여 배포하도록 한다. `python setup.py upload` 커맨드를 사용하지 않고 `twine` 을 사용하는 이유는 `upload` 커맨드는 일반 HTTP를 사용해서 배포하기 때문에 아이디나 패스워드가 노출될 수 있는데 `twine` 은 `TLS` 를 사용하기 때문이다.

그리고 PYPI에 이미 계정이 있어야 하는데, 만일 PYPI 계정이 없다면 `twine` 이 그 또한 가이드 해준다. 아래 커맨드를 사용하여 PYPI에 배포한다.

```bash
twine upload dist/<build_file_name>.whl
```

이제 `pip install <package name>` 을 실행하여 패키지를 어디서든 누구나 인스톨 할 수 있다. 주의할 점은 인스톨은 곧바로 되는데 검색은 PYPI가 인덱스 하는데 시간이 걸린다. 즉 `pip search <package name>` 명령어를 치면 곧바로 검색이 안될 수 있다. 배포한 package 관리는 PYPI 사이트에 로그인해서 해당 package의 페이지로 가면 된다.



#### Tips

- Distutils VS Setuptools
  - `setup.py` 설정을 하도록 해주는 라이브러리는 크게 `distutils`와 `setuptools` 2가지가 있다. `distutils`는 파이썬의 기본 라이브러리에 포함이 되어있고 `setuptools`는 별도로 인스톨을 해야한다. 그래서 `distutils`를 사용하는게 default라고 생각할수 있지만 실제로는 `setuptools`를 사용하는게 default 이다. `distutils`의 단점들을 보완한게 `setuptools`라서 대부분 `setuptools`를 사용하고 있고 파이썬 공식 사이트에서도 `setuptools`를 권장하고 있다.
- Package_data:
  - 만일 파이썬 파일이 아닌 다른 binary 파일을 포함해줘야 한다면 (예를 들어 jar 파일) `setup.py`파일에서 `package_data` 설정을 꼭 해주어야 한다. 이 설정을 잘못하거나 하지 않으면 포함되어야 하는 파일들이 포함이 되지 않은체 빌드가 되서 작동이 잘 되지 않는 경우가 종종있다. 하지만 빌드는 성공하므로 문제가 생길때까지 몰르게 되는 경우가 많다.
  - `zip_safe` 꼭 `False`로 같이 설정 해주어야 한다.
- PYPI에 package를 업로드 한후 검색이 되기까지는 시간이 걸리므로 주의하자. 인스톨은 곧바로 된다.



[출처](https://rampart81.github.io/post/python_package_publish/)