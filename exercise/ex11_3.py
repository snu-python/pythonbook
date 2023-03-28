#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex11_3.py
Description...: Sample solution for exercise 11-3.
                This program demonstrates how to parse texts using a function
                to process numeric data from a text file.
"""
__author__ = 'Jinsoo Park'
__credits__ = '정한비'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def hours_week(dataset, country):
    """평균 주당 노동시간을 구하는 함수다.

    Args:
        dataset (list[dict]): 전처리한 adult 데이터 세트
        country (str): 출신 국가

    Returns:
        float: 평균 주당 노동시간을 소수점 두 자리에서 반올림한 실수
    """
    hours = []                                  # 주당 노동시간을 담을 리스트를 초기화한다.
    for d in dataset:                           # dataset 안 딕셔너리를 차례로 추출한다.
        # 'native-country'의 매핑값이 전달인자와 같으면
        if d.get('native-country') == country:
            # 'hours-per-week'의 매핑값을 가져와서 정수로 변환한다.
            hours.append(int(d.get('hours-per-week')))
    return round(sum(hours) / len(hours), 2)    # 평균을 구한 후 반올림해서 반환한다.


# adult_US.txt 파일을 열어 파일 안 각 줄을 문자열 객체로 갖는 리스트를 반환한다.
lines = open('adult_US.txt', encoding='utf-8').read().splitlines()

adult_data = []  # 데이터를 담을 리스트를 초기화한다.

header = (       # 키(key)로 사용할 열의 제목을 모아둔 튜플
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'martal-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
)

for line in lines:                           # 각 줄을 차례로 하나씩 추출하여
    if not line:                             # 값이 없으면 for 문을 빠져 나온다.
        break
    row_list = line.split(',')               # 줄마다 ',' 기준으로 분할한다.
    for index, item in enumerate(row_list):  # 그 항목들을 하나씩 추출하여
        row_list[index] = item.strip()       # 앞뒤 공백을 제거한다.

    row_dict = {}                            # 각 줄의 정보를 담을 딕셔너리를 초기화한다.
    for col_name in header:                  # header의 키를 하나씩 꺼낸다.
        # 키와 매핑값을 row_dict로 저장한다.
        row_dict[col_name] = row_list[header.index(col_name)]
    adult_data.append(row_dict)              # 해당 사전을 adult_data에 추가한다.

# ----- 인터프리터 모드에서 실행할 경우에만 실행된다 ------------------------------------ #
if __name__ == '__main__':
    test_data = 'United-States', 'Cuba', 'Mexico'  # 테스트용 데이터를 튜플로 만든다.
    for i in test_data:
        print(f'{i} 출신 사람들의 평균 주당 노동시간: {hours_week(adult_data, i)}')

# !!!!! END of ex11_3.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
