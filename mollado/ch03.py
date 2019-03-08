#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ch03.py
Description...: Sample solution for Real Python of Chapter 3.
                This program demonstrates how to use the random module and 
                list.
"""
__author__ = 'Jinsoo Park'
__credits__ = '이재환'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'

import random                        # random 모듈을 불러온다.

questions = [                        # 질문을 담은 리스트
    '제일 좋아하는 과일이 뭐야? ',
    '과일은 뭐니 뭐니 해도 빨갛고 둥글어야지. 어떤 과일 좋아해? ',
    '아니, 사과 몰라? 제일 좋아하는 과일이 뭐냐니깐? '
]

# 질문을 담은 리스트의 첫 번째 질문을 물어보고, 입력한 값을 answer에 할당한다.
answer = input(questions[0]) 

while True:                         # 무한 루프
    if answer == '사과':             # 입력한 값이 '사과'이면 
        break                       # 무한 루프를 종료한다
    
    # 질문을 담은 리스트 중 임의의 질문을 물어보고, 입력한 값을 answer에 할당한다.
    answer = input(random.choice(questions)) 

# 원하는 답인 '사과'를 입력했을 때 '답.정.너'의 반응을 출력한다.    
print ("맞아, 사과가 세상에서 제일 맛있어.") 

# !!!!! END of ch03.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
