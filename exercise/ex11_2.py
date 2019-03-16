#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex11_2.py
Description...: Sample solution for exercise 11-2.
                This program demonstrates how to append text to an existing
                file.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


# zen.txt 파일을 '추가' 모드로 열어서 형식대로 작자와 제목을 입력하고 파일을 닫는다.
with open('zen.txt', mode='a', encoding='utf-8') as file:
    file.write('\n\n{} - {}'.format('Tim Peters', 'The Zen of Python'))

# 수정된 파일을 다시 열어서 새줄바꿈 부호를 삭제한 각 줄을 문자열 객체로 갖는 리스트를 반환한다.
lines = open('zen.txt', mode='r', encoding='utf-8').read().splitlines()

for line in lines :                     # for문을 이용해 리스트의 각 줄을 차례로 추출해서
    print(line)                         # 출력한다.

# !!!!! END of ex11_2.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
