#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex11_1.py
Description...: Sample solution for exercise 11-1.
                This program demonstrates how to use for...in statement to
                count a specific word from a text file.
"""
__author__ = 'Jinsoo Park'
__credits__ = '정한비'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


lines = open('고향의봄.txt', encoding='utf-8').readlines()

count = 0                                   # count 값을 0으로 설정한다.
for line in lines :                         # 각 문장을 추출하기 위해 for문을 사용한다.
    count += line.count('꽃')                # 문장마다 '꽃'의 개수를 더해 재할당한다.

print(count)                                # count를 출력한다.

# !!!!! END of ex11_1.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
