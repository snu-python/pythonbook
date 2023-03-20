#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex8_5.py
Description...: Sample solution for exercise 8-5.
                This program demonstrates how to use while statement. The
                same result with for statement can be found in exercise 8-6.
                The same result with exception handling can also be found in
                exercise 8-7.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.11'
__email__ = 'snu.python@gmail.com'


# 과일 목록을 튜플(리스트도 가능)로 만들어 변수 fruits에 할당한다.
fruits = '사과', '딸기', '블루베리', '바나나', '포도'

# 검색할 과일을 입력받아서 변수 target에 할당한다.
target = input('과일 이름을 입력하세요...: ')
index = 0                         # 튜플의 인덱스로 사용할 센티널 값을 초기화해서 i에 할당한다.
while index < len(fruits):        # 튜플의 인데스 0부터 n-1까지 전체 리스트를 순회한다.
    if fruits[index] == target:   # 검색하는 과일이 리스트에 있다면
        # 리스트에서의 위치를 출력한 후 while문을 빠져 나간다
        print(f'{target}는 과일 목록의 {index + 1}번째에 존재합니다.')
        break
    index += 1                    # 인덱스를 1 증가시켜 다음 객체와 비교할 수 있도록 한다.
else:  # 튜플을 모두 순회한 후 검색하는 과일이 없다면 목록에 없다고 출력하고 while문을 종료한다.
    print(f'{target}는 과일 목록에 존재하지 않습니다.')

# !!!!! END of ex8_5.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
