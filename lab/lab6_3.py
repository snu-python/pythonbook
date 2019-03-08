#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab6_3.py
Description...: Sample solution for Lab 6-3.
                This program demonstrates tuple operations.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


t = 'a', (1, 2), [(10, 9), '한글날'], -15   # 튜플을 생성하여 변수 t에 할당한다.
print(type(t))                            # t의 자료형을 출력한다.
print(t)                                  # 변수 t를 출력한다.
t1 = t[1:3]                               # t의 2, 3번 객체를 추출해서 변수 t1에 할당한다.
print(t1)                                 # 변수 t1을 출력한다.
_, *t2, _ = t                             # 더미변수 _와 시퀀스형 패킹 연산자를 사용한다.
print(t2)                                 # 변수 t2를 출력한다.

# !!!!! END of lab6_3.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
