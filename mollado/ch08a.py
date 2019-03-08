#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ch08a.py
Description...: Sample solution for Real Python of Chapter 8.
                This program demonstrates how to draw simple images.
Dependencies..: matplotlib, Pillow
"""
__author__ = 'Jinsoo Park'
__credits__ = '이재환'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


from PIL import Image, ImageDraw    # 이미지를 처리하는데 사용하는 라이브러리
from matplotlib import pyplot       # 화면에 이미지, 그래프를 출력하기 위한 라이브러리

# RGB 색깔을 사용할 수 있는 하얀색 배경의 가로 2, 세로 2 크기의 이미지를 생성한다.
img = Image.new("RGB", (2, 2), 'white')

dctx = ImageDraw.Draw(img)          # Image 객체 위에 그림을 그리는 인스턴스를 생성한다.

dctx.point([(0, 0)], fill='red')        # 0, 0 위치에 빨간색을 칠한다.
dctx.point([(1, 0)], fill='blue')       # 1, 0 위치에 파란색을 칠한다.
dctx.point([(1, 1)], fill='black')      # 1, 1 위치에 검은색을 칠한다.

pyplot.imshow(img)                      # Image 객체를 화면에 출력하기 위해 준비한다.
pyplot.grid(False)                      # 화면에 출력할 때 격자무늬를 표시하지 않는다.
pyplot.show()                           # 화면에 출력한다.

# !!!!! END of ch08a.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
