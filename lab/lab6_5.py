#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab6_5.py
Description...: Sample solution for Lab 6-5.
                This program demonstrates how to use dictionary methods.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


d = dict.fromkeys(['국어', '음악'], 0)  # 매핑값이 0인 딕셔너리를 생성한다.
print(d)                              # 변수 d를 출력한다.
d.setdefault('체육')                   # 키가'체육'이고 매핑값이 None인 객체 쌍을 추가한다.
print(d)                              # 변수 d를 출력한다.
d.update(미술=94)                      # 키가'미술'이고 매핑값이 94인 객체 쌍을 추가한다.
print(d)                              # 변수 d를 출력한다.
d.update(국어=95, 체육=91)              # '국어' 점수를 95로, '체육' 점수를 91로 갱신한다.
d['음악']=83                           # '음악' 점수를 83으로 갱신한다.
print(d)                              # 변수 d를 출력한다
x = d.pop('체육')     # 키가 '체육'인 객체 쌍을 삭제하면서, '체육'의 매핑값을 변수 x에 할당한다.
print(x)                              # 변수 x를 출력한다.
print(d)                              # 변수 d를 출력한다.
print(d.get('미술'))                   # 키가 '미술'인 객체 쌍의 매핑값을 출력한다.
print(d['미술'])                       # 키가 '미술'인 객체 쌍의 매핑값을 출력한다.
print(d.keys())                       # d의 모든 키를 출력한다.
print(tuple(d.values()))              # d의 매핑값을 모두 튜플로 변환해서 출력한다.
print(list(d.items()))                # d의 카와 매핑값 쌍을 모두 리스트로 변환해서 출력한다.

# !!!!! END of lab6_5.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
