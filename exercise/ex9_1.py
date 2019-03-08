#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex9_1.py
Description...: Sample solution for exercise 9-1.
                This program demonstrates how to use try-except statement. The
                same result with while statement can be found in exercise 8-5.
                The same result with for statement can also be found in
                exercise 8-6.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


# 과일 목록을 리스트로 만들어 변수 fruits에 할당한다.
fruits = ['사과', '딸기', '블루베리', '바나나', '포도']

# 검색할 과일을 입력받아서 변수 target에 할당한다.
target = input('과일 이름을 입력하세요...: ')

try:                    # target이 fruits 안에 있는지 확인한다.
    index = fruits.index(target)
except ValueError:      # target이 fruits 안에 없으면 예외를 발생시키다.
    print('과일 목록에 존재하지 않습니다.')
else:                   # target이 fruits 안에 있다면 인덱스 번호에 1을 더해서 출력한다.
    print('과일 목록의 {}번째에 존재합니다.'.format(index + 1))

# !!!!! END of ex9_1.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
