"""
Requests 요청 정보 Payload
1. 세션 활성화 및 비 활성화
2. 쿠키 정보 전송
3. User-Agent 정보 전송
4. 수신 상태 코드 확인
"""

import requests

# 세션 활성화
s = requests.Session()
r = s.get("https://www.naver.com")

# 수신 데이터
# print(r.text)

# 수신 상태 코드
print("Status Code: {}".format(r.status_code))

# 확인
print("OK?: {}".format(r.ok))


# 세션 비활성화
s.close()
