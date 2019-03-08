#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab12_2.py
Description...: Sample solution for Lab 12-2.
                This program demonstrates how to define and use a subclass.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'

from lab12_1 import Dog                 # 반려견(Dog) 클래스를 불러온다.

class Puppy(Dog):
    """반려견(Dog) 클래스의 하위 클래스인 강아지 클래스다."""

    # --- 초기화 메소드 -------------------------------------------------------- #
    def __init__(self, name, dog_type='불명', age=0):
        """Puppy 인스턴스를 초기화하는 메소드다.

        name....: 반려견 이름(문자열)
        dog_type: 반려견 종류(문자열), 기본값은 '불명'
        age.....: 반려견 나이(정수), 기본값은 0
        Returns.: None
        """
        super().__init__(name, dog_type, age)

    # --- 일반 메소드 ---------------------------------------------------------- #
    def speak(self):   # 반려견 메소드를 재정의한다.
        """강아지 짖는 소리를 출력하는 메소드다.

        Returns: 강아지 짓는 소리(문자열)
        """
        print(self.name(), '콩콩')  # 강아지 짖는 소리

# ----- 인터프리터 모드에서 실행할 경우에만 실행됨 ------------------------------------- #
if __name__ == '__main__':
    mypup1 = Puppy('벼리', '코코스파니엘')  # 이름과 종류를 지정하고 인스턴스를 생성한다.
    print(mypup1.name())                # 강아지 이름을 확인한다.
    print(mypup1.dog_type())            # 강아지 종류를 확인한다.
    print(mypup1.age())                 # 강아지 나이를 확인한다.
    mypup1.speak()                      # 강아지가 짖는다.
    mypup2 = Puppy('예달')               # 이름만 지정하고 인스턴스를 생성한다.
    print(mypup2.name())                # 강아지 이름을 확인한다.
    print(mypup2.dog_type())            # 강아지 종류를 확인한다.
    print(mypup2.age())                 # 강아지 나이를 확인한다.
    mypup2.speak()                      # 강아지가 짖는다.

# !!!!! END of lab12_2.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
