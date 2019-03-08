#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab9_1.py
Description...: Sample solution for Lab 9-1.
                This program demonstrates how to use an infinite loop with
                exception handling for the user input.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


while True:
    try:
        i = int(input('1-9 사이의 숫자를 입력하세요...: '))
        if type(i) == int and 0 < i < 10:
            print('통과하셨습니다.')
            break
        else:
            raise ValueError   # ValueError()와 같다
    except ValueError:
        print('ValueError: 1-9 사이의 숫자를 입력하세요!!!')

# !!!!! END of lab9_1.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
