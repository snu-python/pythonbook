#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab6_2.py
Description...: Sample solution for Lab 6-2.
                This program demonstrates how to use list methods.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


L = list('abcaadc')                     # list() 생성자를 사용하면 간단하다.
print(L)                                # 변수 L을 출력한다.
L.append([1, 2])                        # 리스트 마지막에 하나의 객체로 추가한다.
L.insert(1, 'x')                        # 리스트의 두 번째 객체로 'x'를 추가한다.
print(L)                                # 변수 L을 출력한다.
L.remove('a')                           # 첫 번쨰 나타나는 'a'를 삭제한다.
print(L)                                # 변수 L을 출력한다.
L.pop()                                 # 리스트의 마지막 객체를 반환한 후 삭제한다.
print(L)                                # 변수 L을 출력한다.
L.count('a')                            # 리스트에 있는 'a'의 개수를 반환한다.
L.sort(reverse=True)                    # 리스트를 내림차순으로 정렬한다.
print(L)                                # 변수 L을 출력한다.

# !!!!! END of lab6_2.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
