#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex3_2.py
Description...: Sample solution for exercise 3-2.
                This program demonstrates how to use input() and print()
                functions and also shows how to convert data types and
                process string concatenation.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'

name = input('이름을 입력하세요...: ')   # input() 함수를 사용해 변수 name에 값을 할당한다.
print('안녕', name)                   # 인사말을 출력한다.

age = input('몇 살이세요? ')           # input() 함수를 사용해 변수 age에 값을 할당한다.
# age = int(input('몇 살이세요? '))      # 정수로 변환한 후 변수 age에 값을 할당한다.
print('내년에 ' + str(int(age) + 1) + '살이 되시는군요.')     # 문자열을 결합해서 출력한다.
# print('내년에 ' + str(age + 1) + '살이 되시는군요.')  # 문자열을 결합해서 출력한다.

print('Bye~~~!')

# !!!!! END of ex3_2.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
