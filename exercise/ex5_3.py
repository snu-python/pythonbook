#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex5_3.py
Description...: Sample solution for exercise 5-3.
                This program demonstrates how to use string slicing and
                concatenation to encrypt string.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'

first = ''                  # 암호화할 문자열의 처음에 오는 부분 문자열
second = ''                 # 암호화할 문자열의 중간에 오는 부분 문자열
third = ''                  # 암호화할 문자열의 마지막에 오는 부분 문자열

s = input('암호화하려는 문자열을 입력하세요 : ')

first = s[1::3]             # 두 번째 문자부터 세 구간씩 이동하면서 추출한 문자열을 반환한다.
second = s[::3]             # 첫 번째 문자부터 세 구간씩 이동하면서 추출한 문자열을 반환한다.
third = s[2::3]             # 세 번째 문자부터 세 구간씩 이동하면서 추출한 문자열을 반환한다.

encrypted = first + second + third  # 추출한 부분 문자열을을 결합니다.
print(encrypted)                    # 암호화된 문자열을 출력한다.

# !!!!! END of ex5_3.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
