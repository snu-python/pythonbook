#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex10_2.py
Description...: Sample solution for exercise 10-2.
                This program defines a function that accepts a list or a
                tuple containing various data types, and returns a tuple of
                non-numeric data types.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def no_number(seq):
    """숫자가 아닌 자료형을 반환하는 함수다.

    Args:
        seq (list | tuple): 리스트나 튜플

    Returns:
        tuple: 숫자가 아닌 자료형을 담은 튜플
    """
    nonumeric = []                      # 숫자가 아닌 자료형을 담을 리스트를 초기화한다.

    for i in seq:
        if type(i) == int or type(i) == float:  # 정수나 실수이면
            continue                            # 건너뛴다.
        nonumeric.append(i)                     # 정수나 실수가 아니면 리스트에 추가한다.

    return tuple(nonumeric)                     # 튜플로 변환해서 반환한다.


# ----- 인터프리터 모드에서 실행할 경우에만 실행된다 ------------------------------------ #
if __name__ == '__main__':
    test_data = [[1], {1}, 1, '1', 'one', -3.14, {'1': 1}, 0, '2.58', (5, 9.9)]
    result = no_number(test_data)
    print('테스트 데이터.:', test_data)
    print('결과........:', result)

# !!!!! END of ex10_2.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
