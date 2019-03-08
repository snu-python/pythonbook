#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab11_3.py
Description...: Sample solution for Lab 11-3.
                This program demonstrates how to read a text file and to
                convert string into dictionary type using eval(). It then
                computes grades from the converted data type(i.e., dictionary).
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


data = []                           # 딕셔너리 데이터를 담을 리스트 data를 만든다.

with open('grades.txt', encoding='utf-8') as file:  # with문으로 파일을 연다.
    for line in file:                               # for문을 사용해서 한 줄씩 꺼낸다.
        # eval() 함수로 문자열을 딕셔너리로 변형하여 리스트에 추가한다.
        data.append(eval(line))

for grade in data:                    # for문을 통해 data에서 딕셔너리를 하나씩 추출한다.
    result = (grade['중간고사'] * 0.8   # 딕셔너리 키로 중간고사와 기말고사 성적을 얻는다.
              + grade['기말고사'] * 1.2) / 2                    # 최종 성적을 계산한다.
    print('{}의 최종 성적 : {}'.format(grade['학생'], result))    # 최종 성적을 출력한다.

# !!!!! END of lab11_3.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!