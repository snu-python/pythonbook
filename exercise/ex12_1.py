#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex12_1.py
Description...: Sample solution for exercise 12-1.
                This program demonstrate how to create a simple class with
                instance attributes and class methods. It also demonstrate
                how to instantiate and use instances. In addition it shows
                how to use docstrings defined in the class definition.
"""

__author__ = 'Jinsoo Park'
__credits__ = '김기석'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


class Vector2D:
    """2차원 실수 평면 위의 벡터(점)를 구현한 클래스다.

    속성.: __x_point, __y_point
    메소드: distance(), dot()
    사용법:
        >>> v1 = Vector2D('3', 4.0)
        >>> v1.distance()
        5.0
        >>> v2 = Vector2D(1, 2)
        >>> v2.dot(v1)
        11.0
    """

    # --- 초기화 메소드 -------------------------------------------------------- #
    def __init__(self, x, y):
        """인스턴스를 생성할 때 x와 y 좌표를 전달받아 초기화하는 메소드다.

        x......: x 좌표(실수)
        y......: y 좌표(실수)
        Returns: None
        사용법...:
            >>> v1 = Vector2D('1', '2')
            >>> v2 = Vector2D(1, 2)
            >>> v3 = Vector2D(1.0, 2.0)
            >>> v4 = Vector2D(1, 2.3)
            >>> v5 = Vector2D(1.2, '2')
        """
        try:                            # 전달인자를 실수형으로 변환해서 인스턴스 속성에 할당한다.
            self.__x_point = float(x)   # 인스턴스 속성: x 좌표
            self.__y_point = float(y)   # 인스턴스 속성: y 좌표
        except ValueError:
            print('ERROR: x 좌표와 y 좌표 모두 숫자일 때만 정의됩니다.')

    # --- 일반 메소드 ---------------------------------------------------------- #
    def distance(self):
        """해당 벡터(점)와 원점 사이의 거리를 반환하는 메소드다.

        Returns: 원점으로부터의 거리(실수)
        사용법...:
            >>> v1 = Vector2D(3, 4)
            >>> v1.distance()
            5.0
        """
        return (self.__x_point ** 2 + self.__y_point ** 2) ** (1 / 2)

    def dot(self, other):
        """Vector2D 클래스의 다른 인스턴스와의 내적을 반환하는 메소드다.

        other..: Vector2D 클래스의 인스턴스
        Returns: 두 Vector2D 클래스 인스턴스간의 내적(실수)
        사용법...:
            >>> v1 = Vector2D(3, 4)
            >>> v2 = Vector2D(1, 2)
            >>> v2.dot(v1)
            11.0
        """
        try:
            return self.__x_point * other.__x_point + self.__y_point * other.__y_point
        except Exception:
            print('ERROR: Vector2D 클래스 인스턴스가 아닙니다.')


# ----- 인터프리터 모드에서 실행할 경우에만 실행됨 ------------------------------------- #
if __name__ == '__main__':
    print('Vector2D.__doc__')
    print(Vector2D.__doc__)             # Vector2D 클래스의 설명문자열을 출력한다.
    print("v1 = Vector2D('3', 4.0)")
    v1 = Vector2D('3', 4.0)             # Vector2D 인스턴스 v1을 생성한다.
    print('v1.distance()')
    print(v1.distance())                # 원점으로부처의 v1 거리를 구한다.
    print('v2 = Vector2D(1, 2)')
    v2 = Vector2D(1, 2)                 # Vector2D 인스턴스 v2를 생성한다.
    print('v2.dot(v1)')
    print(v2.dot(v1))                   # v2와 v1의 내적을 구한다.
    print('v2.dot(3)')
    v2.dot(3)                           # v2와 정수 3의 내적을 구하기 때문에 오류가 난다.
    print("v3 = Vector2D('line', 2)")
    v3 = Vector2D('line', 2)            # Vector2D 인스턴스 v3의 좌표에 문자열이 있어 오류가 난다.

# !!!!! END of ex12_1.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
