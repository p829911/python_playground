#!/bin/bash

DAY=`date +%w`

if [ $DAY -eq 3 ]; then
	echo "오늘은 수요일입니다."
elif [ $DAY -eq 4 ]; then
	echo "오늘은 목요일입니다."
else
	echo "수요일 또는 목요일이 아닙니다."
fi
