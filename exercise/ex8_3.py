#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex8_3.py
Description...: Sample solution for exercise 8-3.
                This program demonstrates how to use while statement. The
                same result with for statement can be found in exercise 8-4.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'

import math                                         # math 모듈을 불러온다.

i = 0                                               # 변수 i를 정수로 선언하고 초깃값을 0으로 설정한다.
while i < 10:                                       # i 값을 0부터 9까지 순회한다.
    print('{}! = {}'.format(i, math.factorial(i)))  # i의 계승 값을 계산해 출력한다.
    i += 1                                          # i에 1을 더한다.
else:                                               # while문이 정상적으로 종료되면
    print('종료')                                    # '종료'를 출력하고 while문을 빠져나간다.

# !!!!! END of ex8_3.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
