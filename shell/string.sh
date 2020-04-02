#!/bin/bash

echo -n "프로그램을 설치하겠습니까? (yes|no) : "
read ANS

if [ $ANS = yes ]; then
	echo "설치했습니다."
elif [ $ANS = no ]; then
	echo "설치하지 못했습니다."
else
	echo "똑바로 입력하십시오"
fi
