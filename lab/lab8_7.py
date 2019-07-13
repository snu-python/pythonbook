#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab8_7.py
Description...: Sample solution for Lab 8-7.
                This program demonstrates how to use break and continue in a
                loop.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


numbers = [1, 4, 7, 3, 8, -1, 0, 5, 22, 2, 31]

for i in numbers:
    if i < 0:           # i가 음수면
        break           # for문을 종료한다.
    elif i % 2 == 0:    # i가 짝수면
        continue        # 건너뛴다.
    else:               # i가 홀수면
        print(i)        # 그 값을 출력한다.

# !!!!! END of lab8_7.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
