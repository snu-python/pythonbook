#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex5_2.py
Description...: Sample solution for exercise 5-2.
                This program demonstrates how to use single quotes,
                double quotes, the escape character inside strings.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'

print('=' * 5, '삼중 따옴표로 문자열 리터럴을 만든다', '=' * 30)
print('''President Barack Obama said, 
 "Don't just play on your phone, 
\tprogram it."''')

print('=' * 5, '작은 따옴표로 문자열 리터럴을 만든다', '=' * 30)
print('President Barack Obama said,\n "Don\'t ju€€st play on your phone,'
      '\n\tprogram it."')

print('=' * 5, '큰 따옴표로 문자열 리터럴을 만든다', '=' * 31)
print("President Barack Obama said,\n \"Don't just play on your phone,\n\tprogram it.\"")

# !!!!! END of ex5_2.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
