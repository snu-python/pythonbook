#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab8_5.py
Description...: Sample solution for Lab 8-5.
                This program demonstrates how to use a for statement to
                count vowels in English. The same result using a while
                statement can be found in lab8_3.py
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


text = 'Perfection requires the hand of time'  # 문자열을 변수 text에 할당한다.
print(text)                                    # 변수 text를 출력한다.

count = 0                                      # 모음 개수를 세기 위한 변수를 초기화한다.
for char in text:                              # 변수 text 안의 각 문자가
    if char in ['a', 'e', 'i', 'o', 'u']:      # 모음이면
        count += 1                             # count 변숫값을 1 증가시킨다.
else:                                          # 문자열의 모든 문자를 순회한 후에
    print(count)                               # 모음의 개수를 출력한다.

# !!!!! END of lab8_5.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
