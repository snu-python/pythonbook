#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex11_5.py
Description...: Sample solution for exercise 11-5.
                This program demonstrates how to parse texts using a function
                to process numeric data from a text file.
"""
__author__ = 'Jinsoo Park'
__credits__ = '정한비'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


def customer_stat(dataset, job, avg_age=True):
    """고객의 직업에 따른 평균 나이 또는 평균 전화 지속 시간을 출력하는 함수다.

    Args:
        dataset (list[str]): 전처리한 bank 데이터 세트
        job (str): 고객의 직업
        avg_age (bool): True이면 직업별 평균 나이를, False이면 직업별 평균 전화 통화 시간을 계산
    """
    # dataset에 있는 직업군 튜플을 생성한다.
    jobs = (
        'admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management',
        'retired', 'self-employed', 'services', 'student', 'technician',
        'unemployed', 'unknown'
    )

    # 전달인자 job이 해당 직업에 없다면 ValueError를 발생시킨다.
    if job not in jobs:
        raise ValueError('데이터 셋에 없는 직업입니다.')

    result = []  # 나이 또는 전화 통화 시간을 담을 리스트를 초기화한다.

    # 전달인자 job이 해당 직업에 있다면 dataset 안 딕셔너리를 차례로 추출한다.
    for d in dataset:
        if d['job'] == job:  # 딕셔너리의 직업이 전달인자 job과 일치하고
            if avg_age:  # avg_age가 True면 해당 직업의 고객 나이를 추가한다.
                result.append(int(d.get('age')))
            else:        # avg_age가 False면 해당 직업의 고객 통화 시간을 추가한다.
                result.append(int(d.get('duration')))

    if avg_age:  # avg_age가 True면 해당 직업의 고객들 평균 나이를 출력한다.
        print(f'{job} 직업의 평균 나이: {sum(result) / len(result):,.2f}')
    else:        # avg_age가 False면 해당 직업의 고객들 평균 나이를 출력한다.
        print(f'{job} 직업의 평균 통화 시간: {sum(result) / len(result):,.2f}')

bank_data = []   # 각 행의 데이터를 담을 리스트를 초기화한다.

# bank.csv 파일을 열어 파일 안 각 줄을 문자열 객체로 갖는 리스트를 반환한다.
lines = open('bank.csv', mode='r', encoding='utf-8').read().splitlines()

# 파일 첫 번째 줄 값에서 양 끝의 큰따옴표를 제거한 후 키(key)로 사용할 열 제목을 리스트에 할당한다.
header = lines[0].replace('"', '').split(';')

for line in lines[1:]:       # 파일의 두 번째 줄부터 차례로 하나씩 추출하여
    row_list = line.replace('"', '').split(';')  # 해당 줄의 큰따옴표를 모두 제거한 후 ';' 기준으로 분할한다.
    row_dict = {}            # 각 줄의 정보를 담을 딕셔너리를 초기화한다.
    for col_name in header:  # header의 키 값을 하나씩 추출하여
        row_dict[col_name] = row_list[header.index(col_name)]  # 키와 매핑값을 row_dict로 저장한다.
    else:
        bank_data.append(row_dict)  # 해당 사전을 bank_data에 추가한다.

# ----- 인터프리터 모드에서 실행할 경우에만 실행된다 ------------------------------------ #
if __name__ == '__main__':
    # 테스트용 튜플 데이터를 튜플로 만든다.
    test_data = ('admin.', True), ('Govern', True), ('housemaid', False)
    for i, j in test_data:
        print(f'테스트 전달인자: job = {i}, avg_age = {j}')
        try:
            customer_stat(bank_data, i, j)
        except ValueError as err:
            print(err)
        print()

# !!!!! END of ex11_5.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
