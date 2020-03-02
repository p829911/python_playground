"""
개발자 도구 송수신 분석
1. 다음 주식 정보 분석
2. Fake-UserAgent 사용
3. Header 정보 삽입
4. 수신 데이터 가공 및 추출
"""

# pip install fake-useragent

# Fake Header 정보 (가상으로 User-agent 생성)
import json
import urllib.request as req
from fake_useragent import UserAgent

ua = UserAgent()
# print(ua.ie)
# print(ua.msie)
# print(ua.chrome)
# print(ua.safari)
# print(ua.random)

# 헤더 정보
headers = {"User-agent": ua.ie, "referer": "https://finance.daum.net/"}

# 다음 주식 요청 URL
url = "http://finance.daum.net/api/search/ranks?limit=10"

# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode("UTF-8")

# 응답 데이터 확인 (Json Data)
# print("res", res)

# 응답 데이터 str -> json 변환 및 data 값 출력
rank_json = json.loads(res)["data"]

# 중간 확인
# print("중간 확인: ", rank_json, '\n')

for elm in rank_json:
    print(
        "순위: {}, 금액: {}, 회사명: {}".format(
            elm["rank"], elm.get("tradePrice"), elm["name"]
        )
    )
