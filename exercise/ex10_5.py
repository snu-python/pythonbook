#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex10_5.py
Description...: Sample solution for exercise 10-5.
                This program demonstrates how to define and use a lambda
                function.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


pair = [
    (2, 'apple'), (1, 'Banana'), (2, 'Banana'), (1, 'grape'),
    (3, 'apple'), (3, 'Orange'), (2, 'Pineapple')
]

# 튜플의 두 번째 객체를 대소문자 구분 없이 오름차순 정렬한 후, 첫 번째 객체를 오름차순으로 정렬한다.
sorted(pair, key=lambda e: (e[1].lower(), e[0]))

# ----- 인터프리터 모드에서 실행할 경우에만 실행된다 ------------------------------------ #
if __name__ == '__main__':
    print('테스트 데이터.:', pair)
    print('결과........:', sorted(pair, key=lambda e: (e[1].lower(), e[0])))

# !!!!! END of ex10_5.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
