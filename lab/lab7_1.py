#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab7_1.py
Description...: Sample solution for Lab 7-1.
                This program demonstrates how to use iterable operators and
                methods.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


scores = [97, 80, 60, 95, 45, 88, 75, 56]
print(scores)

# all() 함수를 사용해서 확인해도 된다(all(scores)).
print(0 in scores)

# 가장 큰 값을 가진 객체를 반환한다.
best_score = max(scores)
print(best_score)

# 가장 작은 값을 가진 객체를 반환한다.
bottom_score = min(scores)
print(bottom_score)

# 가장 높은 점수와 낮은 점수의 차이를 구한다.
difference = best_score - bottom_score
print(difference)

# 성적 점수 리스트의 평균을 구한다.
average = sum(scores) / len(scores)
print(average)

# 성적 점수 리스트를 내림차순으로 정렬한다.
sorted_scores = sorted(scores, reverse=True)
print(sorted_scores)

# 성적 점수를 역순으로 뒤집어 튜플로 만든다 .
reversed_scores = tuple(reversed(sorted_scores))
print(reversed_scores)

# !!!!! END of lab7_1.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
