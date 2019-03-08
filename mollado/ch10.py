"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ch10.py
Description...: Sample solution for Real Python of Chapter 10.
                This program demonstrates how to access and extract HTML
                documents from a target Web page.
"""
__author__ = 'Jinsoo Park'
__credits__ = '이재환'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


# URL에 접속해 내용물(HTML)을 받아오기 위해 필요한 라이브러리
from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup     # HTML 파싱을 위한 라이브러리

# --- URL에 접속해서 HTML문서 일부 출력 ------------------------------------------- #
keyword = '한국어'                         # 위키피디아에서 불러오려는 페이지의 키워드

# keyword를 URL 형식에 맞게 인코딩한다.
url = 'https://ko.wikipedia.org/wiki/' + parse.quote(keyword)

# urlopen() 함수를 통해 웹 페이지를 불러와서 HTML 구조를 BeautifulSoup으로 파싱한다.
source = BeautifulSoup(urlopen(url), 'html.parser')

# 받아온 HTMl 코드 중 300자를 보기 좋게 출력한다.
print(source.prettify()[:300])

# --- 위키피디아 페이지의 목차에 해당하는 내용을 추출 ----------------------------------- #
# li 태그 중 클래스 이름이 toclevel-1인 모든 요소를 탐색하여 변수 target에 저장한다.
target = source.find_all('li', {'class': 'toclevel-1'})

for e in target:                        # 리스트 target에 들어 있는 각 HTML 요소에 대해
    print(e.get_text().strip())         # HTML 코드를 제거하고 내용물 텍스트만 출력한다.

# --- 위키피디아 페이지의 본문에 해당하는 내용을 추출 ----------------------------------- #
# div 태그 중 id가 bodyContent인 첫번째 요소를 탐색하여 변수 body에 저장한다.
body = source.find('div', {'id':'bodyContent'})

# body의 하위에 있는 모든 <p> 태그를 탐색하여 변수 paragraph에 저장한다.
paragraphs = body.find_all('p')

for p in paragraphs:                    # 리스트 paragraphs 안의 각 객체에 대해
    print (p.get_text().strip())        # HTML 코드를 제거하고 내용 텍스트만 출력한다.
#    break                              # 첫 번째 문단만 출력하고 for문을 빠져나온다.

# !!!!! END of ch10.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!