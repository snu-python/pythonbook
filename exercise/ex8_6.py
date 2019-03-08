#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex8_6.py
Description...: Sample solution for exercise 8-6.
                This program demonstrates how to use for statement. The
                same result with while statement can be found in exercise 8-5.
                The same result with exception handling can also be found in
                exercise 8-7.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


# 과일 목록을 리스트로 만들어 변수 fruits에 할당한다.
fruits = ['사과', '딸기', '블루베리', '바나나', '포도']

# 검색할 과일을 입력받아서 변수 target에 할당한다.
target = input('과일 이름을 입력하세요...: ')

# 시작 번호를 1로 설정해서 리스트 전체를 순회한다.
for index, fruit in enumerate(fruits, start=1):
    if fruit == target:  # 검색하는 과일이 리스트에 있다면
        # 리스트에서의 위치를 출력한 후 for문을 빠져 나간다.
        print('과일 목록의 {}번째에 존재합니다.'.format(index))
        break
else:     # 리스트을 모두 순회한 후 검색하는 과일이 없다면
    print('과일 목록에 존재하지 않습니다.')  # 리스트에 없다고 출력하고 for문을 종료한다.

# !!!!! END of ex8_6.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
