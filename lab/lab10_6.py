#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab10_6.py
Description...: Sample solution for Lab 10-6.
                This program demonstrates how to define a value returning
                function with positional arguments and keyword arguments.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def cal(x, y, op='add'):
    """두 변수와 연산 명령을 입력받아 덧셈, 뺄셈, 곱셈, 나눗셈 연산을 하는 계산기 함수다.

    x......: 숫자(정수 또는 실수)
    y......: 숫자(정수 또는 실수)
    op.....: 'add'(기본값), 'sub', 'mul', 'div'
    Returns: 연산 결과(실수)
    """
    if op == 'add':
        return float(x + y)
    elif op == 'sub':
        return float(x - y)
    elif op == 'mul':
        return float(x * y)
    elif op == 'div':
        return x / y            # 실수를 반환하기 때문에 float()을 사용하지 않아도 된다.
    else:
        print('잘못된 연산자입니다.')
        return None             # None을 return할 때는 생략해도 된다.

# ----- 인터프리터 모드에서 실행할 경우에만 실행됨 ------------------------------------- #
if __name__ == '__main__':
    i = cal(10, 7)              # 기본 값으로 더하기 연산을 수행한다.
    print(i)                    # 결과를 출력한다.
    i = cal(3, 4, 'sub')        # 빼기 연산을 수행한다.
    print(i)                    # 결과를 출력한다.
    i = cal(1, 5, op='mul')     # 곱하기 연산을 수행한다.
    print(i)                    # 결과를 출력한다.
    i = cal(1, 2, 'div')        # 나누기 연산을 수행한다.
    print(i)                    # 결과를 출력한다.
    i = cal(10, 7, 'ad')        # 잘못된 연산자를 입력한다.

# !!!!! END of lab10_6.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
