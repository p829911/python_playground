#!/bin/bash

echo -n "Enter a file or directory name : "
read FILENAME

if [ -f $FILENAME ]; then
	ls -l $FILENAME
elif [ -d $FILENAME ]; then
	ls -ld $FILENAME
else
	echo "파일 없음"
fi
