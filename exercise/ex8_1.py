#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex8_1.py
Description...: Sample solution for exercise 8-1.
                This program demonstrates how to use conditional statement.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


city = input('도시 이름을 입력하세요: ')

if city == '서울':                                # city 값이 '서울'이면
    size = 605                                   # 변수 size에 605를 입력한다.
elif city == '파리':                              # city 값이 '파리'이면
    size = 105                                   # 변수 size에 105를 입력한다.
elif city == '에든버러':                           # city 값이 '에딘버러'이면
    size = 264                                   # 변수 size에 264을 입력한다.
else:                                            # 그 이외의 경우에는
    size = 'Unknown'                             # 변수 size에 'Unknown'을 입력한다.

print(f'{city}의 면적은 {size} 평방 킬로미터입니다.')
# print('{}의 면적은 {} 평방 킬로미터입니다.'.format(city, size))

# !!!!! END of ex8_1.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
