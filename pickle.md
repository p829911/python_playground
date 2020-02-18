# pickle file

데이터를 저장하고 불러올때 매우 유용한 라이브러리이다.

list, dictionary 등을 파일 그대로 저장하면 용량이 매우 커지는데 pickle을 사용하면 binary 형태로 저장되기 때문에 용량이 매우 작아진다.

**data를 pickle로 저장하기**

```python
import pickle

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

# save
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
    
# load
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
```

gzip을 이용하여 pickle로 저장된 데이터를 압축하고 해제하는 예제이다. 당연히 대부분은 용량이 매우 줄어든다.

```python
import pickle
import gzip

data = {
    'a': [1, 2.0, 3, 4+6j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

# save and compress
with gzip.open('testPickleFile.pickle', 'wb') as f:
	pickle.dump(data, f)
    
# load and uncompress
with gzip.open('testPickleFile.pickle', 'rb') as f:
    data = pickle.load(f)
```

