"""
사이트 요청 정보 확인
1. encar(엔카) 사이트 정보 수신
2. GET 파라미터 요청
3. 수신 데이터 디코딩(Decoding)
4. 요청 URL 정보 분석
"""

import urllib.request
from urllib.parse import urlparse

# encar 실습
url = "http://www.encar.com"
mem = urllib.request.urlopen(url)

# 여러 정보
print("type: {}".format(type(mem)))
print("geturl: {}".format(mem.geturl()))
print("status: {}".format(mem.status))
print("header: {}".format(mem.getheaders()))
print("getcode: {}".format(mem.getcode()))
print("read: {}".format(mem.read(100).decode("utf-8")))
print("parse: {}".format(urlparse("http://www.encar.co.kr?test=test").query))

# ipify
API = "https://api.ipify.org"

# Get 방식 Parameter
values = {"format": "json"}

print("before param: {}".format(values))
params = urllib.parse.urlencode(values)
print("after param: {}".format(params))

# 요청 URL 생성
URL = API + "?" + params
print("요청 URL = {}".format(URL))

# 수신 데이터 읽기
data = urllib.request.urlopen(URL).read()

# 수신 데이터 디코딩
text = data.decode("UTF-8")
print("response: {}".format(text))
