#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab5_7.py
Description...: Sample solution for Lab 5-7.
                This program demonstrates how to manipulate strings using
                the slicing operator.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


telephone = '0213456789'        # telephone 변수에 문자열 전화번호를 할당한다.
print(telephone)                # telephone 변수를 출력한다.

area_code = telephone[0:2]      # 1~2번째 문자를 추출해서 변수에 할당한다.
print(area_code)                # 결과를 출력한다.

number = telephone[2:]          # 세 번째부터 나머지 문자를 추출해서 변수에 할당한다.
print(number)                   # 결과를 출력한다.

print(type(area_code))          # area_code 변수의 자료형을 출력한다.
print(type(number))             # number 변수의 자료형을 출력한다.

# !!!!! END of lab5_7.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
