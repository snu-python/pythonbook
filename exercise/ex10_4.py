#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex10_4.py
Description...: Sample solution for exercise 10-4.
                This program defines a function that uses in operator
                to find the index of a target object from a sequence.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def search_index(seq, target):
    """시퀀스형 객체 내에 특정 객체(항목)의 인덱스를 반환하는 함수다.

    Args:
        seq (str | list | tuple): 검색 목록(시퀀스형)
        target (obj): 찾고자 하는 객체

    Returns:
        int: 시퀀스형의 인덱스 번호; 만약 특정 객체가 존재하지 않으면 -1을 반환한다.
    """
    if target in seq:                   # seq 안에 target이 있으면
        return seq.index(target)        # target의 인덱스 번호를 반환한다.
    return -1                           # seq 안에 target이 없으면 -1을 반환한다.

# ----- 인터프리터 모드에서 실행할 경우에만 실행된다 ------------------------------------ #
if __name__ == '__main__':
    test_data = (   # 테스트용 데이터를 (seq, target) 형식의 튜플 쌍으로 된 튜플로 만든다.
        ('I love Python', 'p'),
        (['기타', '베이스', '키보드', '드럼'], '드럼'),
        ([1, 2, 3], 1)
    )
    for seq, target in test_data:
        result = search_index(seq, target)
        print('테스트 데이터.:', seq)
        print('타깃........:', target)
        print('결과........:', result, end='\n\n')

# !!!!! END of ex10_4.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
