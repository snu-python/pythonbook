#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab3_4.py
Description...: Sample solution for Lab 3-4.
                This program demonstrates how to convert data types using
                type casting functions.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


# input() 함수를 이용해 number 변수에 값을 할당한 후 그 값을 출력한다.
number = input('1과 10 사이의 아무 숫자를 입력하세요[1~10]: ')
print(number)

number = int(number)    # number를 정수로 변환한 후 number에 재할당한다.
total = number + 11     # number에 11을 더한 후 total 변수에 그 결괏값을 할당한다.
print(total)            # total 변숫값을 출력한다.

# !!!!! END of lab3_4.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
