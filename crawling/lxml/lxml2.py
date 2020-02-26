import requests
from lxml.html import fromstring

# from lxml.html import tostring

# conda install cssselect
# conda install lxml
# conda install requests


def main():
    """
    네이버 메인 뉴스 스탠드 스크래핑 메인 함수
    """
    # 세션 사용
    session = requests.Session()
    response = session.get("https://www.naver.com")  # Get, Post

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)
    print(urls)


def scrape_news_list_page(response):
    # URL 딕셔너리 선언
    urls = {}

    # 태그 정보 문자열 저장
    root = fromstring(response.content)

    for a in root.xpath(
        '//ul[@class="api_list"]/li[@class="api_item"]/a[@class="api_link"]'
    ):
        name, url = extract_contents(a)
        urls[name] = url

    return urls


def extract_contents(dom):
    link = dom.get("href")

    name = dom.xpath("./img")[0].get("alt")

    return name, link


# 스크래핑 시작
if __name__ == "__main__":
    main()
