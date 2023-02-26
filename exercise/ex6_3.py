#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex6_3.py
Description...: Sample solution for exercise 6-3.
                This program demonstrates how to use dictionary operators.
"""
__author__ = 'Jinsoo Park'
__credits__ = '정한비'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


# 물품을 딕셔너리로 정의한다
products = {'수박': 15000, '콩나물': 850, '초콜릿': 1500, '생선': 9000, '파리채': 1000}

del products['수박']                                           # 이전 물품을 제거한다.
del products['파리채']                                          # 이전 물품을 제거한다.

products['감'] = 800                                           # 신상품을 추가한다.
products['전기장판'] = 20000                                     # 신상품을 추가한다.

print('바뀐 물품 내역 :', products)                               # 바뀐 물품 내역을 고시한다.

purchase = input('어떤 물품을 구매하실 예정인가요? ')                 # 구매할 물품을 입력받는다.
print('{}은 {:,}원입니다'.format(purchase, products[purchase]))  # 물품의 가격을 알려준다.

# !!!!! END of ex6_3.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
