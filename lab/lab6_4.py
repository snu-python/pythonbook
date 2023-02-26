#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab6_4.py
Description...: Sample solution for Lab 6-4.
                This program demonstrates how to create, access and delete
                items in the dictionary.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


d = {'짝수': [2, 4, 6, 8], '홀수': [1, 3, 5, 7, 9]}
print(d)                         # 변수 d를 출력한다.
print(len(d))                    # d에 몇 개의 객체가 있는지 확인한다.
d['소수'] = [2, 3, 5, 7]          # 딕셔너리에 객체 한 개를 추가한다.
print(d)                         # 변수 d를 출력한다.
print('짝수' in d)                # '짝수' in d.keys()와 같다.
del d['짝수']                     # 키가 '짝수'인 객체를 삭제한다.
print(d)                         # 변수 d를 출력한다.
print(d['홀수'][-1])              # 키가 '홀수'인 객체의 매핑값에서 마지막 객체를 추출한다.

# !!!!! END of lab6_4.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
