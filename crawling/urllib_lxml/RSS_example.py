"""
행정안전부 사이트 RSS 데이터 수신
1. RSS 란?
2. 반복문을 활용한 연속 요청
3. 요청 URL 정보 분석
4. 수신 XML 데이터 확인
"""

import urllib.request
import urllib.parse

# 행정 안전부: https://www.mois.go.kr
# 행정 안전부 RSS API URL
# https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1012
API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

# 중간 확인
print(params)

# 연속해서 4회 요청
for c in params:
    # URL 인코딩
    param = urllib.parse.urlencode(c)

    # URL 완성
    url = API + "?" + param

    # 요청
    res_data = urllib.request.urlopen(url).read()

    # 수신 후 디코딩
    content = res_data.decode("UTF-8")
    print(content)
