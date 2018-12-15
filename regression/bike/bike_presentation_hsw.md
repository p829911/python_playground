<p style="text-align: center; font-size: 50pt; font-weight: Bold; color: navy; font-family: D2Coding;"> Bike Sharing Demand </p>
<br>
<br>

![image](https://user-images.githubusercontent.com/17154958/50039509-15e5ca00-0077-11e9-8ca5-43fcb83b238e.png)

<br>
<p style="text-align: center; font-size: 30pt; font-weight: Bold; font-family: D2Coding;"> 현승우 </p>

---
# 데이터 탐색
![image](https://user-images.githubusercontent.com/17154958/50039749-b689b900-007a-11e9-8ed3-7128b435f506.png)

#### train shape: 10886, 12
#### test shape: 6493, 9
- test에서는 렌탈 수와 관련된 Casual, Registered, Count가 빠짐

---
# Feature

![image](https://user-images.githubusercontent.com/17154958/50039709-e1bfd880-0079-11e9-8250-c864f5798a6d.png)

---

# Feature

![image](https://user-images.githubusercontent.com/17154958/50039712-f4d2a880-0079-11e9-9716-9d9a1f157640.png)

---
# 초기 설정
```
import pandas as pd
import seaborn as sns
import datetime
import statsmodels.api as sm
from statsmodels.graphics import utils
from sklearn.model_selection import KFold
%matplotlib inline
mpl.rc('figure', figsize=(8, 5))
mpl.rc('figure', dpi=100)
```
---
# EDA

```
train.datetime = pd.to_datetime(train.datetime)
test.datetime = pd.to_datetime(test.datetime)
train['day'] = train.datetime.apply(lambda x: x.day)
test['day'] = test.datetime.apply(lambda x: x.day)
train['weekday'] = train.datetime.apply(lambda x: x.weekday())
test['weekday'] = test.datetime.apply(lambda x: x.weekday())
train['hour'] = train.datetime.apply(lambda x: x.hour)
test['hour'] = test.datetime.apply(lambda x: x.hour)
train['year'] = train.datetime.apply(lambda x: x.year)
test['year'] = test.datetime.apply(lambda x: x.year)
train['month'] = train.datetime.apply(lambda x: x.month)
test['month'] = test.datetime.apply(lambda x: x.month)
```
- 문자열 형식인 datetime을 카테고리칼 변수로 만들어주는 코드
---
```
train.isnull().sum()
```
- null 변수는 없음


![image](https://user-images.githubusercontent.com/17154958/50039819-47ad5f80-007c-11e9-85b3-8cf0e1046c12.png)

---
### season과 count의 boxplot

![image](https://user-images.githubusercontent.com/17154958/50039824-63b10100-007c-11e9-8bff-e2319533d960.png)

---
### day와 count의 boxplot

![image](https://user-images.githubusercontent.com/17154958/50039846-cd310f80-007c-11e9-92b6-52e4e7596fb1.png)

---
### weekday와 count의 boxplot

![image](https://user-images.githubusercontent.com/17154958/50039862-f356af80-007c-11e9-882c-4ddddd8427b8.png)

---
### hour와 count의 boxplot
- holiday 기준

![image](https://user-images.githubusercontent.com/17154958/50039874-08334300-007d-11e9-8738-76dc296e4277.png)

---
### hour와 count의 boxplot
- workingday 기준

![image](https://user-images.githubusercontent.com/17154958/50039879-1e410380-007d-11e9-8cc2-bc529be49a08.png)

---
- 위의 두 그래프로 working day일 때는 출퇴근 시간에 사람들의 자전거 이용이 많았고
- 일하지 않는 날에는 오후 시간대에 자전거 이용량이 많았다
- 또한 holiday와 그래프의 분포가 거의 비슷하고 holiday의 정보가 workingday에 포함되므로
- holiday 변수를 OLS 모델에 포함시키지 않는다.

---
### weather의 countplot

![image](https://user-images.githubusercontent.com/17154958/50039933-70ceef80-007e-11e9-9ff3-e49e6f2b89d6.png)

- 날씨가 제일 안좋은 날인 4번은 train 데이터에 1개 들어있음 (나중에 교차검증 때 문제가 되었음)

---
### temp와 count의 jointplot
- temp와 count는 0.4의 상관관계를 가짐

![image](https://user-images.githubusercontent.com/17154958/50039976-0f5b5080-007f-11e9-87c9-1d8995615967.png)

---
### atemp와 count의 jointplot
- atemp와 count는 0.39의 상관관계를 가짐

![image](https://user-images.githubusercontent.com/17154958/50040022-87c21180-007f-11e9-973c-fb20c9ee0124.png)

---
### atemp와 temp의 scatter plot
![image](https://user-images.githubusercontent.com/17154958/50040117-cf956880-0080-11e9-95df-f1b985ce547e.png)

- atemp가 12.12인 195개의 데이터의 체감온도를 계산하여 넣음
- (수정)temp가 25인 것 중 atemp가 12.12인 24개의 데이터만 바꿔줬어야 했을 것 같음

---
### 체감온도 계산
- 현재 사용하고 있는 체감온도 산출식은 2001년 8월 캐나다 토론토에서 열린 **Joint Action Group for Temperature Indices(JAG/TI)회의**에서 발표된 것으로 미국과 캐나다 등 북아메리카 국가들을 중심으로 **최근에 가장 널리 사용되고 있음**

$$
\text{atemp} = 13.12 + 0.625T - 11.37V^{0.16} + 0.3965V^{0.16}T
$$
$$
T: \text{temp (celcius)}
$$
$$
V: \text{windspeed (km/h)}
$$

- [체감온도 산출법](https://www.kma.go.kr/HELP/basic/help_01_07.jsp)

---
### 바람세기

![image](https://user-images.githubusercontent.com/17154958/50040336-cf976780-0084-11e9-93aa-1c174c979ace.png)

- 체감온도를 다시 계산하고 체감온도 계산법에 바람세기가 들어가므로 바람세기를 OLS 모델에 추가하지 않는다.

---
### 수정된 atemp와 temp의 scatter plot

![image](https://user-images.githubusercontent.com/17154958/50040350-28ff9680-0085-11e9-8df2-80df546d298b.png)

- 체감 온도와 기온의 상관관계가 0.99므로 atemp만 OLS 모델에 포함시킨다.
---
### 습도의 distplot

![image](https://user-images.githubusercontent.com/17154958/50040381-a0cdc100-0085-11e9-84a7-723ba0b0a5b7.png)

- 0인 습도는 존재할 수 없다.

---
### 습도가 0인 데이터 처리
- 2011년 3월 10일 22개의 데이터가 0
- 3월 10일과 같은 날씨 3의 시간별 습도 평균을 각각 구하여 데이터에 넣어 주었다.

---
### 습도가 0인 데이터 처리

![image](https://user-images.githubusercontent.com/17154958/50040499-e5f2f280-0087-11e9-950b-f78be5dbbdc8.png)

---
### 처리 후 습도의 distplot

![image](https://user-images.githubusercontent.com/17154958/50040508-133fa080-0088-11e9-9ad4-3ed61de6bd29.png)

---
### count의 distplot

![image](https://user-images.githubusercontent.com/17154958/50040556-07081300-0089-11e9-9f69-90e868b7b111.png)

- 분포가 왼쪽으로 치우쳐있어 log를 줘서 정규분포 형태에 가깝게 만들어준다.
---
### np.log1p(count)의 distplot

![image](https://user-images.githubusercontent.com/17154958/50040546-d922ce80-0088-11e9-86a0-a0903e1378e0.png)

---
### OLS.from_formula

![image](https://user-images.githubusercontent.com/17154958/50040641-d7f2a100-008a-11e9-8368-c17e3fc841c7.png)

<p style="text-align: left; font-size: 15pt; font-weight: Bold; font-family: D2Coding;">* model = sm.OLS.from_formula('np.log1p(count) ~ C(season) + C(workingday) + scale(atemp) + scale(humidity) + C(weekday) + C(weather) + C(hour) + C(month) + C(year) + 0', data=train)
</p>

---
### OLS Summary

![image](https://user-images.githubusercontent.com/17154958/50040812-c959b900-008d-11e9-9582-d9ff06d3af46.png)

- 조건수가 7.62e + 15로 굉장히 높다.
- 수정.
---
### season과 month의 상관관계
- 당연히 month가 있으면 season은 넣어줄 필요가 없다는 것을 생각하지 못했다.

![image](https://user-images.githubusercontent.com/17154958/50040854-94019b00-008e-11e9-84eb-e73192432edd.png)

---
### 수정한 OLS
![image](https://user-images.githubusercontent.com/17154958/50040871-d75c0980-008e-11e9-839a-28a3f7c51fc2.png)

- 조건수가 117로 크게 줄었다.

---
### 계수 부분

![image](https://user-images.githubusercontent.com/17154958/50040904-594c3280-008f-11e9-9702-08a2fbf39fef.png)

---
### 교차 검증
- weather 4인 데이터가 1개 밖에 존재하지 않기 때문에
- 그 데이터가 test데이터에 들어갈 때 문제가 될 수 있다.
- 그렇기 때문에 행 번호 5631의 데이터를 삭제한 후 교차검증을 실시 하였다.

<br>

![image](https://user-images.githubusercontent.com/17154958/50040940-cd86d600-008f-11e9-989b-181ab1cb8d01.png)

---
<p style="text-align: center; font-size: 50pt; font-weight: Bold; color: navy; font-family: D2Coding;"> 감사합니다. </p>

















