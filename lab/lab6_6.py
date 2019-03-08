#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab6_6.py
Description...: Sample solution for Lab 6-6.
                This program demonstrates how to use set operators and methods.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


set1 = {'a', 'b', 'c'}                  # {}를 사용해서 세트를 생성한다.
print(set1)                             # set1을 출력한다
set2 = set('bcdef')                     # set() 생성자를 사용해서 세트를 생성한다.
print(set2)                             # set2를 출력한다.

# set1 & set2은 set1.intersection(set2) 또는 set2.intersection(set1)와 같다.
set3 = set1 & set2
print(set3)                             # set3을 출력한다.
print(set3 < set1)                      # set3.issubset(set1)과 같다.
set3.update({1, 2, 3})                  # set3 |= {1, 2, 3}과 같다.
print(set3)                             # set3을 출력한다.

# !!!!! END of lab6_6.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
