#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab10_4.py
Description...: Sample solution for Lab 10-4.
                This program demonstrates how to create a void function.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def draw_triangle(char):
    """높이와 밑변이 5인 직각 삼각형 도형을 그리는 함수다.

    char...: 도형 부호 문자(문자열)
    Returns: None
    """
    for i in range(1, 6):    # range() 클래스를 이용해서 다섯 번 순회하도록 한다.
        print(char * i)      # char를 차례대로 1부터 5까지 반복 결합해서 출력한다.

# ----- 인터프리터 모드에서 실행할 경우에만 실행됨 ------------------------------------- #
if __name__ == '__main__':
    draw_triangle('*')
    draw_triangle('@')

# !!!!! END of lab10_4.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
