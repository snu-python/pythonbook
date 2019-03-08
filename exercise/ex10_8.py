#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex10_8.py
Description...: Sample solution for exercise 10-8.
                This program demonstrates how to use the variable-length
                argument tuples (* operator with positional arguments, which
                is also called sequence data packing operator). The function
                accepts arbitrary number of strings and returns a list
                containing strings sorted by their lengths in descending order.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def compare_texts(text1, text2):
    """두 문장을 비교하여 중복되는 단어의 개수를 반환하는 함수다.

    text1..: 첫 번째 문장이나 텍스트(문자열)
    text2..: 두 번째 문장이나 텍스트(문자열)
    Returns: 중복된 단어를 키로, 중복 횟수를 매핑값으로 하는 딕셔너리
    """
    import string           # 문장에 있는 부호들을 처리하기 위해 string 클래스를 불러온다.

    result = {}             # 결과를 담을 딕셔너리를 초기화한다.

    # string 클래스의 punctuation에 있는 모든 부호를 문장과 하나씩 비교해서 문장에 있는
    # 부호들을 제거한다.
    for t in string.punctuation:
        text1 = text1.replace(t, '').lower()
        text2 = text2.replace(t, '').lower()

    # 문장 부호를 제거한 문자열을 단어별로 분리하여 리스트로 저장한다.
    text1 = text1.split(' ')
    text2 = text2.split(' ')

    # --- 같은 단어를 확인하는 순환문 ---------------------------------------------- #
    for index1, word1 in enumerate(text1):          # text1의 단어들을 하나씩 선택하고
        for index2, word2 in enumerate(text2):      # text2의 단어들을 하나씩 선택하여
            if word1 == word2:                      # 선택된 두 단어가 같으면
                # result 딕셔너리에 해당 키(key)가 있을 때에는 중복 횟수만 1 증가시킨다.
                result[word1] = result.get(word1, 0) + 1
                text1[index1] = None                # 같은 단어의 중복 확인을 방지하는
                text2[index2] = None                # 코드
                break
            else:                                   # 선택한 두 단어가 다르면
                continue                            # 순환문을 계속 실행한다.
    return result                                   # 결과 딕셔너리를 반환한다.


# ----- 인터프리터 모드에서 실행할 경우에만 실행됨 ------------------------------------- #
if __name__ == '__main__':
    test_data = [
        ('apple is an apple!!!', 'this is not an apple!'),
        ('Python is the best computer language! but I do '
         'not prefer Python than Java for some purpose.',
         'Sometimes, Java is more powerful than Python '
         'language. but I recommend Python for scientific '
         'purpose.')
    ]

    for t1, t2 in test_data:
        result = compare_texts(t1, t2)
        print('테스트 데이터 1:', t1)
        print('테스트 데이터 2:', t2)
        print('결과........:', result)
        print()

# !!!!! ex10_8.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
