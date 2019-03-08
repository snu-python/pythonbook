#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex6_2.py
Description...: Sample solution for exercise 6-2.
                This program demonstrates how to convert a tuple to a list and
                to use list methods as well.
"""
__author__ = 'Jinsoo Park'
__credits__ = '정한비'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'

# 튜플형으로 정의한다.
basket = ('바지', '치마', '니트', '책', '니트', '치마', '바지', '바지', '니트',
          '치마', '책', '필통')

basket_list = list(basket)          # 내용을 수정하기 위해 튜플 bastket을 리스트로 변환한다.
del basket_list[-1]                 # 마지막 목록을 제거한다.

in_basket = input('어떤 물품을 확인하시겠습니까(있으면 True, 없으면 False)? ')
print(in_basket in basket_list)     # 불린으로 물품이 목록에 있는지 확인한다.

# !!!!! END of ex6_2.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
