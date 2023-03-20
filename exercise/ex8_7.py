#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex8_7.py
Description...: Sample solution for exercise 8-7.
                This program demonstrates how to use break and continue
                statement in infinite loop using random module.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.11'
__email__ = 'snu.python@gmail.com'


import random                           # random 모듈을 불러온다.

i = 0                                   # 변수 i의 초깃값을 0으로 설정한다.
while True:                             # 무한 루프로 순회한다.
    i = random.randint(1, 9)            # 1~9 사이의 임의의 정수를 생성해서 i에 할당한다.
    if i <= 5:                          # i가 5이하면
        print(i)                        # i를 출력하고
        continue                        # 다시 임의의 정수를 생성하기 위해 while문의 처음으로 돌아간다.
    print(f'{i}: 무한루프에서 빠져나갑니다.')   # i가 5이하가 아니면 i를 출력하고
    break                               # 무한 루프를 종료한다.

# !!!!! END of ex8_7.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
