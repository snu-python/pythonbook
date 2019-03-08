"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ch11.py
Description...: Sample solution for Real Python of Chapter 11.
                This program demonstrates how to access and extract json
                format data from a target Web page using fake online REST API.
"""
__author__ = 'Jinsoo Park'
__credits__ = '이재환'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


from urllib.request import urlopen      # 인터넷 접속에 사용하는 라이브러리
from wordcloud import WordCloud         # 워드 클라우드를 생성하기 위한 라이브러리
from matplotlib import pyplot           # 워드 클라우드를 화면에 출력하기 위한 라이브러리
import json                             # JSON 처리를 위한 라이브러리를 호출한다.

# ---  사이트에 접속에 데이터를 가져와 출력 ------------------------------------------- #
url = 'https://jsonplaceholder.typicode.com/posts?userId=1'
response = urlopen(url)                     # url에 접속을 요청해 결과를 받아온다.
source = response.read().decode('utf-8')    # 받아온 결과를 utf-8 인코딩으로 읽어온다.
print(source[:550])                         # 첫 550 글자를 읽어온다.


# -- 포스팅한 글을 추촐한 후 출력 -------------------------------------------------- #
parsed = json.loads(source)  # JSON으로 작성한 문자열을 딕셔너리로 갖는 리스트로 변환한다.

posts = []                   # 포스팅한 글 내용을 담을 리스트를 초기화한다.
for d in parsed:             # 리스트에 있는 각 딕셔너리(사용자가 포스팅한 글 정보)에 접근하여
    posts.append(d['body'])  # 글 내용을 담고있는 body 부분만 posts 리스트에 저장한다.

text = ' '.join(posts)       # 리스트의 문자열들을 공백을 이용해 문자열 하나로 병합한다.
print(text)                  # 문자열 하나로 병합한 결과를 출력한다.

# --- 워드 클라우드로 변환 ------------------------------------------------------- #
wc = WordCloud().generate(text)             # 텍스트를 워드 클라우드로 변환한다.

# --- 워드 클라우드를 화면으로 출력 ------------------------------------------------ #

pyplot.figure(figsize=(12,12))      # 화면에 출력할 때 가로 12, 세로 12의 크기로 출력한다.

# 가로, 세로 두 배치를 이용해서 워드클라우드를 그린다(화면에 출력하지는 않는다).
pyplot.imshow(wc, interpolation='bilinear')

pyplot.axis('off')                  # 가로 축, 세로 축을 화면에 표시하지 않는다.
pyplot.show()                       # 그려진 워드 클라우드를 실제로 화면에 출력한다.

# !!!!! END of ch11.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!