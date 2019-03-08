#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex3_1.py
Description...: Sample solution for exercise 3-1.
                This program demonstrates how to use input() and print()
                functions and also shows how to convert data types and
                process string concatenation.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'

season = input('좋아하는 계절을 무엇인가요? ')  # input() 함수로 변수 eason에 값을 할당한다.
print(season)                            # 변수 season을 출력한다.

date = input('며칠에 태어났나요? ')       # input() 함수를 사용해 변수 date에 값을 할당한다.
date = int(date)                      # date의 값을 정수로 변환한 후 date에 재할당한다.
print(date)                           # 변수 date의 자료형을 출력한다.

# 하나의 문자로 결합해서 결과를 출력한다.
print('좋아하는 계절은 ' + season + '이고, ' + str(date) + '일에 태어났습니다.')

# !!!!! END of ex3_1.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
