#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab8_4.py
Description...: Sample solution for Lab 8-4.
                This program demonstrates how to use a for statement with
                range().
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


alist = list(range(1,11))  # 1부터 10까지의 정수를 포함하는 리스트를 변수 alist에 할당한다.
print(alist)               # 변수 alist를 출력한다.
for i in alist:            # alist에 속한 각 정수 i가
    if i % 3 == 2:         # 3으로 나눈 나머지가 2이면
        print(i)           # i를 출력한다.

# !!!!! END of lab8_4.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
