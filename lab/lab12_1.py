#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab12_1.py
Description...: Sample solution for Lab 12-1.
                This program demonstrates how to define and use a custom class.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


class Dog:
    """반려견 클래스다.

    속성.: count, __name, __dog_type, __age
    메소드: name(), dog_type(). age(), speak()
    """
    count = 0                        # 클래스 속성 : 전체 인스턴스 수

    # --- 초기화 메소드 -------------------------------------------------------- #
    def __init__(self, name, dog_type='불명', age=0):
        """Dog 인스턴스를 초기화하는 메소드다.

        name....: 반려견 이름(문자열)
        dog_type: 반려견 종류(문자열), 기본값은 '불명'
        age.....: 반려견 나이(정수), 기본값은 0
        Returns.: None
        """
        self.__name = name           # 인스턴스 속성 : 반려견 이름
        self.__dog_type = dog_type   # 인스턴스 속성 : 반려견 종류
        self.__age = age             # 인스턴스 속성 : 반려견 나이
        Dog.count += 1               # 인스턴스를 생성할 때 1 증가시킨다.

    # --- 일반 메소드 ---------------------------------------------------------- #
    def name(self):
        """반려견 이름을 반환하는 메소드다.

        Returns: 반려견 이름(문자열)
        """
        return self.__name

    def dog_type(self):
        """반려견 종류를 반환하는 메소드다.

        Returns: 반려견 종류(문자열)
        """
        return self.__dog_type

    def age(self):
        """반려견 나이를 반환하는 메소드다.

        Returns: 반려견 나이(정수)
        """
        return self.__age

    def speak(self):
        """반려견 종류에 따라 짖는 소리를 다르게 출력하는 메소드다.

        Returns: 반려견 짓는 소리(문자열)
        """
        if self.__dog_type == '코코스파니엘':
            print('왈왈')
        elif self.__dog_type == '골든리트리버':
            print('월월 ')
        else:
            print('멍멍')

# ----- 인터프리터 모드에서 실행할 경우에만 실행됨 ------------------------------------- #
if __name__ == '__main__':
    mydog1 = Dog('코코')         # 이름만 지정하고 나머지는 기본값을 가진 인스턴스를 생성한다.
    print(mydog1.name())        # 반려견 이름을 확인한다.
    print(mydog1.dog_type())    # 반려견 종류를 확인한다.
    print(mydog1.age())         # 반려견 나이를 확인한다.
    mydog1.speak()              # 반려견이 짖는다.
    mydog2 = Dog('보라', '코코스파니엘', 2)  # 이름/종류/나이를 지정해서 인스턴스를 생성한다.
    print(mydog2.name())        # 반려견 이름을 확인한다.
    print(mydog2.dog_type())    # 반려견 종류를 확인한다.
    print(mydog2.age())         # 반려견 나이를 확인한다.
    mydog2.speak()              # 반려견이 짖는다.

# !!!!! END of lab12_1.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
