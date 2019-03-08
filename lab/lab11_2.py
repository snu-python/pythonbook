#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab11_2.py
Description...: Sample solution for Lab 11-2.
                This program demonstrates how to read a text file using
                read(), readline(), readlines() methods in combination with
                while, for, and with statements.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


# --- Use of read() method -------------------------------------------------- #
file = open('grades.txt', encoding='utf-8')   # 파일을 연다.
print(file.read())                            # read() 메소드로 읽은 파일을 출력한다.
file.close()                                  # 파일을 닫는다.

# --- Use of readline() method in while loop -------------------------------- #
file = open('grades.txt', encoding='utf-8')   # 파일을 읽기 모드로 연다.

while True:                         # while문을 활용해서 한 줄씩 출력한다.
    line = file.readline()          # 파일에서 한 줄씩 읽어오려고 readline()을 사용한다.
    if not line:                    # 파일을 다 읽고 빈 문자열이 나타난다면
        break                       # while문을 종료한다.
    print(line.rstrip())            # 두 번 줄 바꿈하는 것을 막으려고 rstrip()을 사용한다.
file.close()                        # 파일을 닫는다.

# --- Use of readlines() method in for loop --------------------------------- #
file = open('grades.txt', encoding='utf-8')   # 파일을 읽기 모드로 연다.
lines = file.readlines()            # 파일을 줄단 위로 읽어오려고 readlines()를 사용한다.
for line in lines:                  # for문으로 리스트에 저장한 데이터를 한 줄씩 출력한다.
    print(line, end='')             # 두 번 줄 바꿈을 막으려고 end=''로 처리한다.
file.close()                        # 파일을 닫는다.

# --- Use of for loop in with syntax ---------------------------------------- #
with open('grades.txt', encoding='utf-8') as file:   # with문으로 파일을 연다.
    for line in file:               # for문을 사용해서 한 줄씩 추출한다.
        print(line.rstrip())        # 두 번 줄 바꿈을 막으려고 rstrip()을 사용한다.
        
# !!!!! END of lab11_2.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!