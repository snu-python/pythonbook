#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ch08b.py
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

grid = [                            # 각 좌표에 칠할 색깔 정보를 담고 있는 리스트
    (0, 1, 0, 1, 0),
    (1, 0, 1, 0, 1),
    (0, 1, 0, 1, 0),
    (1, 0, 1, 0, 1),
    (0, 1, 0, 1, 0)
]

colors = ['#f9f9f9', '#000000']     # 색깔 정보를 담고 있는 리스트

# RGB 색깔을 사용할 수 있는 하얀색 배경의 가로 5, 세로 5 크기의 이미지를 생성한다.
img = Image.new("RGB", (5, 5), "white")

dctx = ImageDraw.Draw(img)          # Image 객체 위에 그림을 그리는 인스턴스를 생성한다.

for i, coordinate in enumerate(grid):       # grid를 줄 단위로 읽어온다.
    for j, code in enumerate(coordinate):   # grid에서 가져온 줄 값을 하나씩 읽어온다.
        dctx.point([(j, i)], fill=colors[code])     # 좌표 (j, i)에 색깔을 칠한다.

pyplot.imshow(img)                  # Image 객체를 화면에 출력하기 위해 준비한다.
pyplot.grid(False)                  # 화면에 출력할 때 격자무늬를 표시하지 않는다.
pyplot.show()                       # 화면에 출력한다.

# !!!!! END of ch08b.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
