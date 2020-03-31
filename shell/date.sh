#! /bin/bash
# 'date' 명령어 연습

echo "올해가 시작한 뒤로 지금까지 `date +%j` 일이 지났습니다."
# 날짜를 형식화 하려면 포매터 앞에 '+'를 써야 한다.
# %j 는 오늘이 연중 몇 번째 날인가를 알려준다.

echo "1970/01/01 이후로 지금까지 `date +%s` 초가 지났습니다."
# %s 는 "UNIX 에폭 (epoch)" 이 시작한 뒤로 현재까지 몇 초가 지났는지 알려준다.

prefix=temp
suffix=`eval date +%s` # 'date'의 "+%s" 옵션은 GNU 전용 옵선이다.
filename=$prefix.$suffix
echo $filename
# "유일한" 임시 파일 이름으로 $$를 쓰는 것보다 더 좋다.

