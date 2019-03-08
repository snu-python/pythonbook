#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab5_6.py
Description...: Sample solution for Lab 5-6.
                This program demonstrates how to manipulate strings with
                whitespace.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


# 삼중 따옴표를 사용하면 따옴표 안에 작은따옴표나 큰따옴표를 사용할 수 있을 뿐만 아니라,
# \n을 넣지 않고도 여러 줄로 이루어진 문자열 리터럴을 표현할 수 있다.
text = '''"She's gone! Yon' Heathcliff's run off wi' her!" gasped the girl.
"That is not true!" exclaimed Linton, rising in agitation.'''
print(text)

# 이스케이프 문자를 사용해도 되지만 가독성이 낮아지는 단점이 있다.
text = ('\"She\'s gone! Yon\' Heathcliff\'s run off wi\' her!\" gasped'
        ' the girl.\n\"That is not true!\" exclaimed Linton, rising'
        ' in agitation.')
print(text)

# !!!!! END of lab5_6.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
