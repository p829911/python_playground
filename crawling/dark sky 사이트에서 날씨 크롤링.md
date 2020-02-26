# dark sky 사이트에서 날씨 크롤링하기

https://darksky.net/dev 다음 사이트를 이용해 api로 날씨 데이터를 크롤링 해 볼 것이다.

dark sky api는 전 세계 현재/과거/미래에 관련된 날씨와 관련된 많은 데이터들을 제공한다. 사이트에 가입 후 console로 들어가면 다음과 같은 창이 나타난다.

![image](https://user-images.githubusercontent.com/17154958/50571619-5c1a8780-0df2-11e9-91d5-533200f96c72.png)

Your Secret Key에 있는 key를 사용하여 dark sky로 쿼리를 날려야 한다.

![image](https://user-images.githubusercontent.com/17154958/50571671-034bee80-0df4-11e9-9a9e-c5d435cc3e2b.png)

dark sky api 는 하루에 1000건의 무료 call을 제공하고 있으며 1건이 추가 될 때마다 $0.0001를 받고 있다. 1000건이 넘는 요청을 해야 할 경우 account setting에서 카드 등록을 하고 하루 최대 call수를 늘려주면 요청이 정상적으로 된다.


이 포스트 에서는 구글 맵을 이용하여 지역 명으로 위도 경도를 얻은 후 그 위도 경도를 이용하여 dark sky에 요청하여 날씨 정보를 받는 실습을 진행해 보았다.



자세한 코드는 아래 링크에서 확인 가능하다.

https://github.com/p829911/python_study/blob/master/crawling/dark_sky_weather_crawling.ipynb
