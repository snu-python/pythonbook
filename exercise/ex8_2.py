#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex8_2.py
Description...: Sample solution for exercise 8-2.
                This program demonstrates how to use conditional statement.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


# 판매 총액을 입력받아 변수 sales에 할당한다.
sales = int(input('회사의 판매 총액은 얼마입니까? '))

# 관리 비용을 입력받아 변수 expense에 할당한다.
expense = int(input('회사의 관리 비용은 얼마입니까? '))

operating_income = sales - expense     # 영업 이익을 계산한다(판매 총액 - 관리비용).

if operating_income >= 0:              # 영업 이익이 적자가 아니면 영업 이익을 출력한다.
    print('영업 이익은 {:,}원입니다.'.format(operating_income))
else:                                  # 영업 이익이 적자이면 괄호로 묶어 출력한다.
    print('영업 이익은 ({:,})원입니다.'.format(abs(operating_income)))

# !!!!! END of ex8_2.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
