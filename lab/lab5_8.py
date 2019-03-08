#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab5_8.py
Description...: Sample solution for Lab 5-8.
                This program demonstrates how to manipulate strings using
                the slicing and concatenation operators.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


str1 = 'I'
str2 = 'love'
str3 = 'Python'

str4 = str1 + ' ' + str2 + ' ' + str3  # 각 문자열 사이에 공백을 넣고 합한다.
print(str4)                            # 결과를 출력한다.

str4 = str4[:6]                        # 'I love'라는 문자열만 추출해서 재할당한다.
str5 = str4 + ' ' + 'programming'      # 변수 str4, 공백, 'programming'을 합한다.
print(str5)                            # 결과를 출력한다.

# !!!!! END of lab5_8.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
