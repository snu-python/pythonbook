#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex10_3.py
Description...: Sample solution for exercise 10-3.
                This program defines a function that switch an upper
                letter to a lower letter or vice versa if the letter
                is one of A, B, C, D
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def switch_somecase(text):
    """특정 영어 문자(A, B, C, D)의 대문자를 소문자로, 소문자를 대문자로 바꾼
    새로운 문자열을 반환하는 함수다.

    text...: 알파벳 문자열
    Returns: 특정 대소문자를 반전한 알파벳 문자열
    """
    switch_case = set('ABCDabcd')   # 대소문자 반전할 문자들을 세트로 선언한다.
    switched_text = ''              # 대소문자를 반전한 문자열을 담을 변수를 초기화한다.

    for char in text:
        # 문자가 A', 'B', 'C', 'D', 'a', 'b', 'c', 'd' 중 하나면
        if char in switch_case:
            # 문자 char가 소문자면 대문자로, 대문자면 소문자로 바꾸어
            # switched_text에 결합해 재할당한다.
            switched_text += char.swapcase()
        else:                       # 그 외 문자면
            switched_text += char   # sswitched_text에 그대로 결합해 재할당한다.

    return switched_text            # A/a, B/b, C/c, D/d를 반전한 문자열을 반환한다.

# ----- 리스트로 구현 ------------------------------------------------------------
def switch_somecase2(text):
    """특정 영어 문자(A, B, C, D)의 대문자를 소문자로, 소문자를 대문자로 바꾼
    새로운 문자열을 반환하는 함수다.

    text...: 알파벳 문자열
    Returns: 특정 대소문자를 반전한 알파벳 문자열
    """
    switch_case = set('ABCDabcd')       # 대소문자 반전할 문자들을 세트로 선언한다.
    switched_text = []                  # 대소문자를 반전한 문자들을 담을 리스트를 초기화한다.

    for char in text:
        # 문자가 A', 'B', 'C', 'D', 'a', 'b', 'c', 'd' 중 하나면
        if char in switch_case:
            # 문자 char가 소문자면 대문자로, 대문자면 소문자로 바꾸어 switched_text에 추가한다.
            switched_text.append(char.swapcase())
        else:                           # 그 외 문자이면
            switched_text.append(char)  # switched_text에 그대로 추가한다.

    # switched_text에 있는 모든 문자열 객체를 빈칸으로 결합해서 반환한다.
    return ''.join(switched_text)

# ----- 인터프리터 모드에서 실행할 경우에만 실행됨 ------------------------------------- #
if __name__ == '__main__':
    test_string = 'I am Python. I am not anaconda!!!'
    result = switch_somecase('I am Python. I am not anaconda!!!')
    print('테스트 데이터.:', test_string)
    print('결과........:', result)

# !!!!! END of ex10_3.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
