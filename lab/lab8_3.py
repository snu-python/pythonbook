#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab8_3.py
Description...: Sample solution for Lab 8-3.
                This program demonstrates how to use a while statement to
                count vowels in English.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


text = 'Perfection requires the hand of time'     # 사용할 문자열을 변수 text에 할당한다.
print(text)                                       # 변수 text를 출력한다.

count = 0                                         # 모음 개수를 세기 위한 변수를 초기화한다.
index = 0                                         # 문자열 사용할 인덱스 번호를 초기화한다.
while index < len(text):                          # text에 포함된 문자만큼 순회한다.
    if text[index] in ['a', 'e', 'i', 'o', 'u']:  # 모음이면
        count += 1                                # count 변숫값을 1 증가시킨다.
    index += 1                                    # 문자열 인덱스를 1 증가시킨다.
else:                                             # 문자열의 모든 문자를 순회한 후
    print(count)                                  # 모음 개수를 출력한다.

# !!!!! END of lab8_3.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
