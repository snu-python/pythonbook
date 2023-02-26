#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab6_1.py
Description...: Sample solution for Lab 6-1.
                This program demonstrates how to use list operators.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


list1 = [-3.13, 'school', [1, 2, 3]]    # [] 연산자로 리스트를 생성한다.
print(list1)                            # 변수 list1을 출력한다.
list2 = list('가나다')                    # list 생성자로 리스트를 생성한다.
print(list2)                            # 변수 list2를 출력한다.
list3 = list1 + list2                   # 결합연산자 +로 두 리스트를 결합한다.
print(list3)                            # 변수 list3을 출력한다.
del list3[-2:]                          # 리스트의 마지막 두 객체를 삭제한다.
print(list3)                            # 변수 list3을 출력한다.
list3[1] = '학교'                        # 리스트 두 번째 객체를 '학교'로 교체한다.
'school' in list3                       # 리스트에 'school' 객체가 있는지 확인한다.
print(list3)                            # 변수 list3을 출력한다.

# !!!!! END of lab6_1.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
