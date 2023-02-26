#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab5_4.py
Description...: Sample solution for Lab 5-4.
                This program demonstrates simple arithmetic operations of
                floats.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


x = 21.0         # 변수 x에 21.0을 할당한다.
print(type(x))   # x의 자료형을 출력한다.
x *= 3           # x에 3을 곱한 결괏값을 다시 x에 재할당한다(증강 할당 연산).
print(x)         # x 값을 출력한다(x가 실수라서 결괏값도 실수다).
x -= 10          # x에서 10을 뺀 결괏값을 다시 x에 재할당한다(증강 할당 연산).
print(x % 4)     # x를 4로 나눈 나머지를 출력한다(x가 실수라서 결괏값도 실수다).

# !!!!! END of lab5_4.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
