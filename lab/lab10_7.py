#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab10_7.py
Description...: Sample solution for Lab 10-7.
                This program demonstrates how to define and use a function with
                sequence packing operator *.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def stat_summary(*nums):    # 시퀀스형 패킹 연산자 *를 사용한다.
    """전달인자로 입력한 임의의 정수나 실수의 기본적인 기술 통계를 반환하는 함수다.

    nums...: 쉼표로 분리된 임의의 정수 또는 실수
    Returns: 입력한 숫자의 개수, 총합, 평균, 최댓값, 최솟값(튜플)
    """
    total = 0                                   # 총합을 참조할 변수를 0으로 초기화한다.
    for i in nums:
        if type(i) == int or type(i) == float:  # 전달인자가 정수나 실수면
            total += i                          # 총합에 더한다.
        else:                                   # 전달인자가 정수나 실수가 아니면
            print('잘못된 자료형입니다.')            # 오류 메시지를 출력한다.
            return None
    return len(nums), total, total/len(nums), max(nums), min(nums)

# ----- 인터프리터 모드에서 실행할 경우에만 실행됨 ------------------------------------- #
if __name__ == '__main__':
    result = stat_summary(1, 3, 5.5, 7, 9, -2)  # 전달인자 값이 모두 정상이면
    print(result)  # 결괏값인 튜플을 반환한다.
    result = stat_summary(1.1, '3', 12, -100)  # 전달인자 값 중 하나가 잘못되었을 때

# !!!!! END of lab10_7.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
