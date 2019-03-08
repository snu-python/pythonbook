#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab10_3.py
Description...: Sample solution for Lab 10-3.
                This program demonstrates how to create and use a lambda
                function.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


# [실습 10-2]의 함수를 람다함수로 구현한다.
triangle = lambda base, height: base * height * 0.5

# ----- 인터프리터 모드에서 실행할 경우에만 실행됨 ------------------------------------- #
if __name__ == '__main__':
    print(triangle(4, 5))
    print(triangle(10.5, 7))

# !!!!! END of lab10_3.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
