#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex11_4.py
Description...: Sample solution for exercise 11-4.
                This program demonstrates how to parse texts using a function
                to process numeric data from a text file.
"""
__author__ = 'Jinsoo Park'
__credits__ = '정한비'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def wines(dataset, alcohol, flavonoid):
    """와인 리스트에서 지정한 알코올 도수보다는 낮고, 플라보노이드의 수치는 높은 와인의 개수를 반환하는 함수

    dataset..: 전처리한 wine quality 데이터 세트(리스트)
    alcohol..: 알코올 도수(숫자형)
    flavonoid: 플라보노이드 수치(숫자형)
    Returns..: 추천 와인 개수(정수)
    """
    count = 0                                   # 추천할 와인 개수를 초기화한다.
    try:
        for d in dataset:                       # dataset 안 딕셔너리를 차례로 추출한다.
            # 전달인자와 데이터 세트의 값을 비교해서 만족하면, count에 1 추가한다.
            if d.get('alcohol') < alcohol and d.get('flavonoids') > flavonoid:
                count += 1
        return count                            # 조건을 충족하는 추천 와인 개수를 반환한다.
    except TypeError:                           # 전달인자가 정수나 실수가 아니면
        print('오류입니다. 정수나 실수를 입력하세요!')   # 오류 메시지를 출력한다.


# wine_quality.csv 파일을 열어 파일 안 각 줄을 문자열 객체로 갖는 리스트를 반환한다.
lines = open('wine_quality.csv', mode='r', encoding='utf-8').read().splitlines()

wine_data = []                          # 각 행의 데이터를 담을 리스트를 초기화한다.

header = [                              # 키(key) 값으로 사용할 열 제목을 모아둔 리스트
    'classifier', 'alcohol', 'malic acid', 'ash', 'alcalinity of ash',
    'magnesium', 'total phenols', 'flavonoids', 'nonflavanoid phenols',
    'proanthocyanins', 'color intensity', 'hue', 'OD280/OD315 of diluted wines',
    'proline'
]

for line in lines:                          # 행을 차례로 하나씩 추출하여
    row_list = line.split(',')              # 해당 줄을 ',' 기준으로 분할한다.

    row_dict = {}                           # 각 줄의 정보를 담을 딕셔너리를 초기화한다.
    for col_name in header:                 # header의 키 값을 하나씩 추출한다.
        # 키와 실수형을 변환한 매핑값을 row_dict로 저장한다.
        row_dict[col_name] = float(row_list[header.index(col_name)])
    wine_data.append(row_dict)              # 해당 딕셔너리를 wine_data에 추가한다.

# ----- 인터프리터 모드에서 실행할 경우에만 실행됨 ------------------------------------- #
if __name__ == '__main__':
    test_data = (15, 'a'), (13, 4), (15.5, 3)   # 테스트용 튜플 데이터를 튜플로 만든다.
    for i, j in test_data:
        print('테스트 전달인자: 알코올 도수 = {}, 플라보노이드 수치 = {}'.format(i, j))
        print('추천 와인 수..: {}'.format(wines(wine_data, i, j)))
        print()

# !!!!! END of ex11_4.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
