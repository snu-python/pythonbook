#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex10_7.py
Description...: Sample solution for exercise 10-7.
                This program demonstrates how to use the variable-length
                argument tuples (* operator with positional arguments, which
                is also called sequence data packing operator). The function
                accepts arbitrary number of strings and returns a list
                containing strings sorted by their lengths in descending order.
"""
__author__ = 'Jinsoo Park'
__credits__ = ['이규한']
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def installment(total_price, payment_amount, interest_rate):
    """매달 특정 할부금을 납입한다는 가정 아래 물건 가격을 전부 갚기 위해 필요한 전체 기간을
    월 단위로 계산해서 출력하는 함수다.

    total_price...: 물건 가격(정수)
    payment_amount: 매달 납입할 할부금(정수)
    interest_rate.: 이자율(실수)
    Returns.......: None
    """
    month = 0
    while (total_price > 0):
        total_price = total_price * (1 + interest_rate) - payment_amount
        month += 1
    print('{} 개월'.format(month))


while True:                 # 대화형 모드에서 ex10_7을 import하면 바로 while문이 실행된다.
    # 잘못 입력했을 때 출력하는 오류 메시지다.
    msg_err = '오류 : 잘못된 숫자입니다!'

    # 프로그램을 계속 진행할지 묻는 메시지다.
    msg_continue = '계속하시겠습니까? (1)예 (2)아니요 => '

    try:                                            # 모든 납입은 월말에 이행한다.
        price = int(input('\n구입한 물건의 가격은 얼마입니까(단위 : 원)? '))
        payment_amount = int(input('매달 얼마씩 지불할 예정입니까(단위 : 원)? '))
        interest_rate = float(input('할부금에 대한 이자율은 얼마입니까(단위 : %)? ')) / 100
        if price * interest_rate < payment_amount:  # 이자가 매달 납입하는 할부금보다 적다면
            installment(price, payment_amount,
                        interest_rate)              # 할부 기간을 계산해서 출력한다.
            quit = int(input(msg_continue))         # 프로그램을 계속 실행할지 묻는다.
            if quit == 1:                           # 계속 실행할 때
                continue
            elif quit == 2:                         # 중단할 때
                print('Bye~~~!')
                break
            else:                       # 기타
                print(msg_err)          # 오류 메시지를 출력하고 다시 프로그램을 실행한다.
        else:                                       # 이자가 매달 납입하는 할부금보다 크다면
            print('이자가 할부금보다 높군요. 매월 이자보다 더 많이 지불해야합니다!!!')
            quit = int(input(msg_continue))         # 프로그램을 계속 실행할지 묻는다.
            if quit == 1:                           # 계속 진행할 때
                continue
            elif quit == 2:                         # 중단할 때
                print('Bye~~~!')
                break
            else:                       # 기타
                print(msg_err)          # 오류 메시지를 출력하고 다시 프로그램을 실행한다.
    except ValueError:
        print(msg_err)

# !!!!! END of ex10_7.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
