# Python Flask Tutorial: Full-Featured Web App Part 1 - Getting Started

[Python Flask Tutorial: Full-Featured Web App Part 1 - Getting Started](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)

pyenv로 flask 폴더 생성 후

```bash
pip install flask
vi hello.py
```



```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"
```

터미널 이동 후

```bash
export FLASK_APP=hello.py
flask run
```

![](https://user-images.githubusercontent.com/17154958/52530998-ed660d80-2d51-11e9-8e86-ce28113928c1.png)

위에 보이는 http://127.0.0.1:5000/ or http://localhost:5000/ 에서 결과물을 확인 할 수 있다.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello World</h1>"
```

html 코드를 한 줄 넣어서 홈페이지를 새로고침 하면 바뀌지 않는다.

터미널에서 `CTRL+C`로 flask 실행 중지 후 `flask run` 으로 다시 실행해야 한다.

위의 작업을 하지 않으려면 `Debug mode` 를 사용해야 하는데

```bash
export FLASK_DEBUG=1
```

터미널 창에서 위의 코드를 실행 후 `flask run` 을 통해 flask를 실행해 준다.

![](https://user-images.githubusercontent.com/17154958/52531055-ccea8300-2d52-11e9-8534-8fac5a1cf9e8.png)

실행 후 확인 코드

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Home Page</h1>"
```

홈페이지 내에서 새로고침만 해도 결과물이 바뀐다.

지금까지는 터미널 모드에서 환경변수를 지정해주므로써 flask를 실행하는 방법을 알아 봤고 python을 이용해 직접 실행할 수 있는 방법을 알아보자.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Home Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)
```

지금 까지 작성한 코드 밑에 `if ~` 코드를 추가해 주면 python을 통해 직접 실행 되도록 하는 방법인데 이 경우 터미널에서 

```bash
python hello.py
```

작성만으로 flask를 실행 할 수 있다.

`__name__` 이라는 인자는 Python 을 이용해 직접 실행하면 `__main__` 이 되고 이 module을 다른 장소에서 import 할 경우 `__name__` 이라는 인자는 module 의 이름이 된다 (`hello.py`) 따라서 위의 코드 밑에 추가한 `if ~` 부분은 Python 을 통해 직접 실행할 때만 실행되는 코드이다.

##### about 페이지 추가

localhost:5000/about의 주소로 들어가면 404 response가 나온다 404 response는 페이지가 존재하지 않는다는 소리이다. 이제 about 페이지를 추가해보자.

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
    return "<h1>Home Page</h1>"

@app.route('/about')
def about():
    return "<h1>About Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)
```

두가지 코드를 추가했는데 하나는 home page의 route 하나를 추가하였다. `@app.route('/home')` 또 하나는 `@app.route('/about')` about 페이지를 추가하였다. 이렇게 코드 한줄로 페이지를 쉽게 만들 수 있다.