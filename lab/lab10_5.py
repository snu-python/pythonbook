#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab10_5.py
Description...: Sample solution for Lab 10-5.
                This program demonstrates how to create a value returning
                function that returns two values as a tuple.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def int_divmod(dividend, divisor):
    """두 정수를 전달받아 몫과 나머지 쌍을 반환하는 함수다.

    Args:
        dividend (int): 피제수
        divisor (int): 제수 정수

    Returns:
        tuple: 몫, 나머지

    """
    # dividend를 divisor로 나눈 몫과 나머지를 튜플로 반환한다.
    return dividend // divisor, dividend % divisor

# ----- 인터프리터 모드에서 실행할 경우에만 실행됨 ------------------------------------- #
if __name__ == '__main__':
    x, y = int_divmod(5, 3)
    print(x, y)
    z = int_divmod(10, 2)
    print(z)

# !!!!! END of lab10_5.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
