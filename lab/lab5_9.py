#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab5_9.py
Description...: Sample solution for Lab 5-9.
                This program demonstrates how to use string methods.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


str1 = '\t  나의 살-던 고향은 꽃피는- 산골-\n\t복숭아-꽃 살-구꽃 아-기 진-달래!!!'
str2 = str1.split()                     # 문자열을 화이트스페이스 기준으로 분할한다.
print(str2)                             # str2를 출력한다.
str3 = ' '.join(str2)                   # 공백 하나로 순회형 문자열들을 결합한다.
print(str3)                             # str3을 출력한다.
str4 = str3.rstrip('!')                 # 문자열의 오른쪽 끝 '!'를 모두 삭제한다.
print(str4)                             # str4를 출력한다.
str5 = str4.replace('-', '')            # '-'를 빈 문자열로 모두 교체한다.
print('{:#^50}'.format(str5))           # print(str5.center(50, '#'))과 같다.

# !!!!! END of lab5_9.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
