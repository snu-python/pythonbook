#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ch05.py
Description...: Sample solution for Real Python of Chapter 5.
                This program demonstrates how to use Counter class and
                matplotlib package to visualize the result of text analysis,
                i.e., word count.
Dependencies..: matplotlib
"""
__author__ = 'Jinsoo Park'
__credits__ = '이재환'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'

from urllib.request import urlopen  # 인터넷 접속에 사용하는 라이브러리
from collections import Counter     # 각 단어가 등장한 횟수를 세기 위한 라이브러리
from matplotlib import pyplot       # 화면에 그래프를 출력하기 위한 라이브러리

# --- 데이터 추출 ------------------------------------------------------------- #
# 인터넷에 있는 파일을 열어서 source에 저장한다.
source = urlopen('https://www.w3.org/TR/PNG/iso_8859-1.txt')
# source를 읽어서 utf-8로 디코딩한 텍스트 파일을 저장한다.
text = source.read().decode('utf-8')

print(type(source))                           # source의 자료형을 확인한다.
print(type(text))                             # text의 자료형을 확인한다.
print(text[:100])                             # text에서 100개 문자만 화면에 출력한다.

# --- 대이터 탐색 ------------------------------------------------------------- #
# 텍스트를 단어 단위로 나눠서 분리한 객체들을 갖는 리스트 words를 반환한다.
words = text.split()
print(len(words))           # 총 몇 개의 단어가 텍스트에 들어있는지 화면에 출력한다.
print(words[:10])           # words에서 열 개만 화면에 출력한다.

# --- 데이터 분석 ------------------------------------------------------------- #
top5 = Counter(words).most_common(5)         # 가장 많이 등장한 단어 다섯 개를 추출한다.
print(top5)                                  # top5 내용을 확인한다.

# --- 시각화 ----------------------------------------------------------------- #
# top5 리스트에서 객체(튜플)의 첫 번째 값(단어)을 추출한다.
top5_words = [t[0] for t in top5]
# top5 리스트에서 객체(튜플)의 두 번째 값(출현 횟수)을 추출한다.
top5_frequencies = [t[1] for t in top5]

pyplot.bar(top5_words, top5_frequencies) # 출현 횟수 순서로 막대그래프를 그린다.
pyplot.xlabel('Word')          # x축 이름을 Word로 지정한다.
pyplot.ylabel('Frequency')     # y축 이름을 Frequency로 지정한다.
pyplot.show()                  # 그래프를 화면에 출력한다.

# !!!!! END of ch05.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
