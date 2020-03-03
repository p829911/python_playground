import requests

s = requests.Session()

# 쿠키 Return
r1 = s.get("https://httpbin.org/cookies", cookies={"name": "Kim"})
print(r1.text)

# 쿠키 Set
r2 = s.get("https://httpbin.org/cookies/set", cookies={"name": "Kim2"})
print(r2.text)

# User-Agent 확인
url = "https://httpbin.org"
headers = {"user-agent": "nice-man_1.0.0_win10_ram16_home_chrome"}

# Header 정보 전송
r3 = s.get(url, headers=headers, cookies={"name": "kim2"})
print(r3.text)

s.close()

# With문 사용 권장 -> 파일, DB, HTTP
with requests.Session() as s:
    r = s.get("https://daum.net")
    print(r.text)
    print(r.ok)
