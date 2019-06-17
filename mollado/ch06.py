#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ch06.py
Description...: Sample solution for Real Python of Chapter 6.
                This program demonstrates how to construct networks and
                to visualize them.
Dependencies..: matplotlib, networkx
"""
__author__ = 'Jinsoo Park'
__credits__ = '이재환'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'

import networkx                    # 그래프 구조를 처리하기 위한 라이브러리
from matplotlib import pyplot      # 화면에 그래프를 출력하기 위한 라이브러리

G = networkx.Graph()               # 빈 그래프 인스턴스 G를 선언한다.

G.add_node('A')                    # G에서 A라는 이름을 갖는 노드를 생성한다.
G.add_node('B')                    # G에서 B라는 이름을 갖는 노드를 생성한다.
G.add_node('C')                    # G에서 C라는 이름을 갖는 노드를 생성한다.
G.add_edge('A', 'B')               # G에서 A와 B사이에 엣지를 연결한다.

networkx.draw(G, with_labels=True) # 그래프를 그림으로 변환한다(화면에는 출력되지 않는다).
pyplot.figure(figsize=(5, 5))      # 출력할 그림의 크기를 가로 5, 세로 5로 정의한다.
pyplot.show()                      # 변환한 그림을 실제로 화면에 출력한다.

# --- 노드 자동 생성 기능 데모 ---------------------------------------------------- #
# networkx 라이브러리는 매우 똑똑해서, 만약 그래프에 존재하지 않는 노드를 연결하면 자동으로 노드를
# 생성한다. 위의 코드는 아래의 코드로 간단하게 바꿀 수 있다.

G = networkx.Graph()               # 빈 그래프 인스턴스 G를 선언한다.

G.add_node('C')                    # G에서 C라는 이름을 가진 노드를 생성한다.
G.add_edge('A', 'B')               # G에서 A와 B사이에 엣지를 암묵적으로 연결한다.

# 그래프를 노드 이름을 표시한 그림으로 변환한다(화면에는 출력되지 않는다).
networkx.draw(G, with_labels=True)
pyplot.figure(figsize=(5, 5))      # 출력할 그림의 크기를 가로 5, 세로 5로 정의한다.
pyplot.show()                      # 변환한 그림을 실제로 화면에 출력한다.

# --- 리스트와 튜플을 사용해서 그래프 형성하기 ---------------------------------------- #
G = networkx.Graph()              # 빈 그래프 인스턴스 G를 선언한다.

edges = [                         # 그래프의 연결 정보를 튜플로 저장하고 있는 리스트
    ('A', 'B'), ('B', 'C'), ('C', 'A'),
    ('C', 'D'), ('D', 'E'), ('E', 'A'),
    ('B', 'F'), ('G', 'C'), ('H', 'C')
]

# 리스트에 있는 모든 연결 정보를 그래프 G에 한 번에 추가한다.
G.add_edges_from(edges)           # A부터 H까지 모든 노드를 암묵적으로 생성한다.

# 그래프를 노드 이름을 표시한 그림으로 변환한다(화면에는 출력되지 않는다).
networkx.draw(G, with_labels=True)
pyplot.figure(figsize=(5, 5))     # 출력할 그림의 크기를 가로 5, 세로 5로 정의한다.
pyplot.show()                     # 변환한 그림을 실제로 화면에 출력한다.

# !!!!! END of ch06.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
