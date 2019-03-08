#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab10_1.py
Description...: Sample solution for Lab 10-1.
                This program demonstrates how to use a recursion function.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def plus(n):
    """
    1부터 n까지의 자연수의 합을 반환하는 함수다.

    n......: 자연수
    Returns: 자연수의 합
    """
    if n == 0:                      # 만약 n이 0이면
        return 0                    # 0를 반환한다.
    else:                           # 만약 n이 0이 아니면
        return n + plus(n - 1)      # n과 plus(n-1)의 값을 더한다.

# ----- 인터프리터 모드에서 실행할 경우에만 실행됨 ------------------------------------- #
if __name__ == '__main__':
    print(plus(5))
    print(plus(10))

# !!!!! END of lab10_1.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
