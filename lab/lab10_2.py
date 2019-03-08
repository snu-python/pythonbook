#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab10_2.py
Description...: Sample solution for Lab 10-2.
                This program demonstrates how to create a custom function
                that accepts parameters.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def triangle_area(base, height):    # 두 매개변수를 각각 밑변,높이로 받아서
    """삼각형의 넓이를 구하는 함수다.

    base...: 밑변(숫자형)
    height.: 높이(숫자형)
    Returns: 삼각형의 넓이(실수)
    """
    return base * height * 0.5      # 밑변 * 높이 * 1/2를 반환한다.

# ----- 인터프리터 모드에서 실행할 경우에만 실행됨 ------------------------------------- #
if __name__ == '__main__':
    print(triangle_area(4, 5))
    print(triangle_area(10.5, 7))

# !!!!! END of lab10_2.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
