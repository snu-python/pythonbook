#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex6_1.py
Description...: Sample solution for exercise 6-1.
                This program demonstrates how to use list methods.
"""
__author__ = 'Jinsoo Park'
__credits__ = '정한비'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


stock = ['마법천자문', '논어', '미움받을 용기', '자존감 수업', '채식주의자']  # 현재의 책 목록
print('기존 책 목록 :', stock)                                     # 기존 책을 출력한다.

stock.remove('마법천자문')              # 오래된 책을 삭제한다.
stock.remove('논어')                  # 오래된 책을 삭재한다.

new_books = ['골든아워', '바로 쓰는 파이썬']

stock.extend(new_books)              # 새로운 책을 추가한다.
                                     # stock += new_books와 같다
stock.sort()                         # 책을 가나다 순으로 정렬한다.

print('정리된 책 목록 :', stock)        # 정렬된 책을 출력한다.
print('남아있는 책 권수 :', len(stock))  # 전체 책 권수를 출력한다.

# !!!!! END of ex6_1.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
