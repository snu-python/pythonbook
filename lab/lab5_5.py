#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab5_5.py
Description...: Sample solution for Lab 5-5.
                This program demonstrates how to use the built-in functions
                for integer arithmetic operations.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


x, y = divmod(abs(-27), 5)  # 27을 5로 나눈 ‘몫’과 ‘나머지’를 x와 y에 할당한다.
print(x)                    # x 값을 출력한다.
print(y)                    # y 값을 출력한다.
z = pow(x, 2, y)            # (x ** 2) % y의 결과를 변수 z에 할당한다.
print(z)                    # z 값을 출력한다.
z /= 7                      # z를 7로 나눈 결괏값을 다시 z에 재할당한다.
print(round(z, 3))          # z 값을 소수점 3자리로 반올림해서 출력한다.

# !!!!! END of lab5_5.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
