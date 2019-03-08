#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab8_2.py
Description...: Sample solution for Lab 8-2.
                This program demonstrates how to use a nested conditional
                statement.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


x = 7                                               # 변수 x에 7을 할당한다.
y = 15                                              # 변수 y에 15을 할당한다.
z = 5                                               # 변수 z에 5을 할당한다.

if x > y:                                           # x가 y보다 크면
    if x > z:                                       # x가 z보다 크면
        print(y + z)                                # y + z를 출력한다.
    else:                                           # x가 z보다 크지 않으면
        print(x + y)                                # x + y를 출력한다.
else:                                               # x가 y보다 크지 않으면
    if z > y:                                       # z가 y보다 크면
        print(x + y)                                # x + y를 출력한다.
    else:                                           # z가 y보다 크지 않으면
        print(x + z)                                # x + z를 출력한다.

# !!!!! END of lab8_2.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
