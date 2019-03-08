#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab8_6.py
Description...: Sample solution for Lab 8-6.
                This program demonstrates how to use a for statement with
                enumerate().
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


# 신규 회원 명단을 변수 member_list에 할당한다.
member_list = ['무지', '어피치', '네오', '제이지', '콘', '프로도', '라이언', '튜브']
print(member_list)                  # 변수 member_list를 출력한다.

member_dict = {}                    # 신규 회원을 담을 변수 member_dict를 초기화한다.

for mem_id, name in enumerate(member_list, start=153):
    member_dict[mem_id] = name      # member_dict에 객체 쌍들을 추가한다.

print(member_dict)                  # 변수 member_dict를 출력한다.

# 변수 member_dict를 한 줄씩 출력한다.
for mem_id, name in member_dict.items():
    print('{}: {}'.format(mem_id, name))

# !!!!! END of lab8_6.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
