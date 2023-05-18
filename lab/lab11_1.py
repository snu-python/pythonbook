#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab11_1.py
Description...: Sample solution for Lab 11-1.
                This program demonstrates how to write dictionary objects to
                a text file. It converts objects in dicttionary type to
                string before writing to a file. It also uses with syntax
                when opening a file in the write mode.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.2'
__email__ = 'snu.python@gmail.com'


grades = [  # grades 리스트에 딕셔너리를 저장한다.
    {'이름': 'A', '중간고사': 90, '기말고사': 85},
    {'이름': 'B', '중간고사': 85, '기말고사': 70},
    {'이름': 'C', '중간고사': 70, '기말고사': 85},
    {'이름': 'D', '중간고사': 95, '기말고사': 100},
    {'이름': 'E', '중간고사': 100, '기말고사': 90},
    {'이름': 'F', '중간고사': 65, '기말고사': 70},
    {'이름': 'G', '중간고사': 70, '기말고사': 75},
    {'이름': 'H', '중간고사': 80, '기말고사': 90},
    {'이름': 'I', '중간고사': 60, '기말고사': 65},
    {'이름': 'J', '중간고사': 95, '기말고사': 70}
]

with open('grades.txt', mode='w', encoding='utf-8') as file:
    for data in grades:             # 리스트 grades에 있는 딕셔너리를 하나씩 추출하여
        file.write(str(data))       # 문자열로 자료형을 변환한 후
        file.write('\n')            # 한 줄씩 쓰기 위해 새줄바꿈 문자열을 추가한다.

# !!!!! END of lab11_1.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!