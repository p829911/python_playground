#!/bin/bash

echo -n "나이를 입력하세요: "
read AGE

if [[ $AGE = [0-9]* ]]; then
  if [ $AGE -le 18 ]; then
  	echo "집에 돌아가세요"
  elif [ $AGE -gt 18 ]; then
 	echo "어서오세요"
  fi
else
	echo "나이를 입력하세요"
fi
