#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex10_6.py
Description...: Sample solution for exercise 10-6.
                This program demonstrates how to use the variable-length
                argument tuples (* operator with positional arguments, which
                is also called sequence data packing operator). The function
                accepts arbitrary number of strings and returns a list
                containing strings sorted by their lengths in descending order.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def sort_by_word_length(*words):
    """입력한 단어 중 길이가 긴 순서부터 내림차순으로 정렬하는 함수다.

    만약 단어의 길이가 같다면 그 단어들을 다시 내림차순으로 정렬한다. 그리고 영어 단어라면 대소문자를
    구분해서 내림차순으로 정렬한다.

    Args:
        words (tuple[str]): 단어 목록

    Returns:
        list: 단어 길이로 내림차순 정렬한 리스트
    """
    t = []                          # (길이, 단어)의 튜플을 객체로 담을 리스트를 초기화한다.
    for w in words:                 # 전달인자로 패킹해서 받은 단어들을 차례로 하니씩 꺼내서
        t.append((len(w), w))       # (길이, 단어) 형식의 튜플 객체로 리스트에 추가한다.

    # 리스트의 sort() 메소드를 사용해서 (길이, 단어) 형식의 튜플 객체들을 길이 순으로
    # 내림차순으로 정렬한다. 만약 길이가 같다면 대소문자 등을 구분해서 내림차순으로 정렬한다.
    t.sort(reverse=True)

    sorted_words = []       # 단어 길이 순으로 내림차순 정렬한 단어를 담을 리스트를 초기화한다.
    for length, word in t:  # (길이, 단어) 리스트에서 길이와 단어를 분리해서 각각 변수에 담는다.
        sorted_words.append(word)   # 단어만 순서대로 리스트에 추가한다.

    return sorted_words     # 단어 길이 순으로 내림차순 정렬한 단어를 담을 리스트를 반환한다.

# ----- 인터프리터 모드에서 실행할 경우에만 실행된다 ------------------------------------ #
if __name__ == '__main__':
    result = sort_by_word_length('피아노', '기타', '베이스', '드럼')
    print('테스트 데이터.:', "'피아노', '기타', '베이스', '드럼'")
    print('결과........:', result)
    print()
    result = sort_by_word_length('red', 'blue', 'green', 'brown', 'gray')
    print('테스트 데이터.:', "'red', 'blue', 'green', 'brown', 'gray'")
    print('결과........:', result)

# !!!!! END of ex10_6.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
