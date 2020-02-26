import requests
import lxml.html

# conda install cssselect
# conda install lxml
# conda install requests


def main():
    """
    네이버 메인 뉴스 스탠드 스크래핑 메인 함수
    """
    response = requests.get("https://www.naver.com")  # Get, Post

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)

    for url in urls:
        print(url)


def scrape_news_list_page(response):
    # URL 리스트 선언
    urls = []

    # 태그 정보 문자열 저장
    root = lxml.html.fromstring(response.content)

    for a in root.cssselect(".api_list .api_item a.api_link"):
        url = a.get("href")
        urls.append(url)

    return urls


# 스크래핑 시작
if __name__ == "__main__":
    main()
