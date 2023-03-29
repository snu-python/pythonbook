#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex10_1.py
Description...: Sample solution for exercise 10-1.
                This program defines a function that accepts s English string
                and returns the number of vowels in the string.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def count_vowels(text):
    """영어 단어 또는 문장에 들어 있는 모음의 개수를 반환하는 함수다.

    Args:
        text (str): 영어 텍스트

    Returns:
        int: 모음 개수
    """
    # 영어 모음(대소문자를 구분하지 않기 때문에 소문자로 이루어진 문자열)
    vowels = 'aeiou'

    count = 0                       # 영어 모음 개수를 세는 변수를 초기화한다.

    for char in text:
        if char.lower() in vowels:  # 추출한 문자를 소문자로 바꾼 후 영어 모음 중 하나면
            count += 1              # count를 1 증가시킨다.

    return count                    # 영어 모음 개수를 반환한다.


# ----- 인터프리터 모드에서 실행할 경우에만 실행된다 ------------------------------------ #
if __name__ == '__main__':
    test_data = 'Apples', 'I love Python'           # 테스트용 데이터를 튜플로 만든다.
    for i in test_data:
        result = count_vowels(i)
        print('테스트 데이터.:', i)
        print('결과........:', result, end='\n\n')

# !!!!! END of ex10_1.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
