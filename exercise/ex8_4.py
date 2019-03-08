#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex8_4.py
Description...: Sample solution for exercise 8-4.
                This program demonstrates how to use for statement. The
                same result with while statement can be found in exercise 8-3.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


import math          # math 모듈을 불러온다.

for i in range(10):  # for문과 range() 클래스를 이용해 0부터 9까지의 정수를 생성한다.
    print('{}! = {}'.format(i, math.factorial(i)))  # i의 계승 값을 계산해 출력한다.
else:                                               # for문이 정상적으로 종료되면
    print('종료')                                    # '종료'를 출력하고 for문을 빠져나간다.

# !!!!! END of ex8_4.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
