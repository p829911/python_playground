#!/bin/bash

# expr: 정수에 대한 사칙 연산과 나머지 연산을 위해 사용
# bc: 정수, 실수, 비교, 논리, 사인, 코사인, 탄젠트 등 계산도 가능

expr 1 + 1
expr 2 - 4
expr 2 / 2 
expr 2 \* 2
expr 2 % 2
expr 3 % 2

A=`expr 1 + 1`
echo $A

A=`expr $A \* 4`
echo $A

echo '2*(3+4)' | bc
echo '2-3' | bc
echo '10/3' | bc
echo 'scale=3;10/3' | bc
echo '1024^3' | bc

