#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex12_2.py
Description...: Sample solution for exercise 12-2.
                This program demonstrate how to create a simple class with
                instance attributes and class methods. It demonstrate how to
                instantiate and use instances. It also shows hwo to access
                instance attriutes using methods.
"""

__author__ = 'Jinsoo Park'
__credits__ = '이규한'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'

# ----- Dragon 클래스 정의 ------------------------------------------------------ #
class Dragon:
    """용 클래스다.

    Attributes:
        __name (str): 용의 이름
        __hunger (int): 용의 배고픔 정도
        __fatigability (int): 용의 피로도 정도
        __hygiene (int): 용의 위생상태
        __joy (int): 용의 행복지수
        __affection (int): 용의 사랑지수

    Methods:
        __init__(self, name: str) -> None:
        name(self) -> str:
        hunger(self) -> int:
        fatigability(self) -> int:
        hygiene(self) -> int:
        joy(self) -> int:
        affection(self) -> int:
        status(self) -> None:
        change(self, target: str) -> None:
        next_turn(self) -> None:
    """

    # --- 초기화 메소드 --------------------------------------------------------- #
    def __init__(self, name):
        """용의 이름은 전달된 값으로 초기화하고 나머지 속성들은 0으로 초기화한다.

        Args:
            name (str): 용의 이름
        """
        self.__name = name                          # 인스턴스 속성: 용의 이름
        self.__hunger = 0                           # 인스턴스 속성: 용의 배고픔 정도
        self.__fatigability = 0                     # 인스턴스 속성: 용의 피로도 정도
        self.__hygiene = 0                          # 인스턴스 속성: 용의 위생상태
        self.__joy = 0                              # 인스턴스 속성: 용의 행복지수
        self.__affection = 0                        # 인스턴스 속성: 용의 사랑지수

    # --- 접근자 메소드 --------------------------------------------------------- #
    def name(self):
        """용의 이름을 반환한다.

        Returns:
            str: 용의 이름
        """
        return self.__name

    def hunger(self):
        """용의 배고픔 정도를 반환하는 메소드다.

        Returns:
            int: 용의 배고픔 정도
        """
        return self.__hunger

    def fatigability(self):
        """용의 피로도를 반환하는 메소드다.

        Returns:
            int: 용의 피로도
        """
        return self.__fatigability

    def hygiene(self):
        """용의 위생상태를 반환하는 메소드다.

        Returns:
            int: 용의 위생상태
        """
        return self.__hygiene

    def joy(self):
        """용의 행복지수를 반환하는 메소드다.

        Returns:
            int: 용의 행복지수
        """
        return self.__joy

    def affection(self):
        """용의 사랑지수를 반환하는 메소드이다.

        Returns:
            int: 용의 사랑지수
        """
        return self.__affection

    # --- 일반 메소드 ----------------------------------------------------------- #
    def status(self):
        """용의 상태를 출력하는 메소드다."""
        print('\n[ {}의 신체 상태 ]\n배고픔 = {} | 피로도 = {} | 위생상태 = {}'.format(
            self.__name, self.__hunger, self.__fatigability, self.__hygiene))

    def change(self, target):
        """용의 상태를 바꾸는 메소드다.

        Args:
            target (str): 용의 상태(hunger, fatigability, hygiene, affection, joy)
        """
        if target == 'hunger':
            self.__hunger -= 3
        elif target == 'fatigability':
            self.__fatigability -= 3
        elif target == 'hygiene':
            self.__hygiene -= 3
        elif target == 'affection':
            self.__affection = 1 if self.__affection < 0 else self.__affection + 2
        elif target == 'joy':
            self.__joy = 1 if self.__joy < 0 else self.__joy + 1

    def next_turn(self):
        """게임이 다음 단계로 넘어가면서 용의 전체 상태를 업데이트하는 메소드다."""
        self.__hunger += 1
        self.__fatigability += 1
        self.__hygiene += 1
        self.__joy -= 1
        self.__affection -= 1


# ----- 게임 시작 -------------------------------------------------------------- #
turn = 0                                        # 게임의 최대 횟수를 초기화한다.

mn_game_rule = (                                # 게임 시작 전에 게임 규칙을 설명한다.
    '\n##### 용 키우기 게임 #####\n게임 규칙:\n\t'
    '(1) 배고픔, 피로도, 위생상태가 5에 도달하면, 용은 죽는다.\n\t'
    '(2) 30단계 후, 용은 늙어 죽는다.'
)

mn_action = (                                   # 용에게 시킬 행동을 묻는다.
    '> {}에게 어떤 명령을 내릴까요?\n(1) 먹기, (2) 놀기, (3) 잠자기, '
    '(4) 데이트하기, (5) 씻기\n번호를 입력하세요 => '
)

print(mn_game_rule)                             # 게임 규칙을 출력한다.

name = input('용의 이름을 입력하세요: ')              # 용의 이름을 붙여준다.
dragon = Dragon(name)

while True:
    dragon.status()                             # 용의 현재 상태를 표시한다.

    # 용이 죽을 수 있는 상태를 규정하여 용이 이 상태에 도달하면 게임을 끝낸다.
    if (dragon.hunger() >= 5 or dragon.fatigability() >= 5
            or dragon.hygiene() >= 5 or turn >= 30):
        if dragon.hunger() >= 5:
            print('!!! {}는(은) 아사했습니다. !!!'.format(dragon.name()))
        elif dragon.fatigability() >= 5:
            print('!!! {}는(은) 수면 부족으로 죽었습니다. !!!'.format(dragon.name()))
        elif dragon.hygiene() >= 5:
            print('!!! {0}는(은) 씻지 못해서 죽었습니다. !!!'.format(dragon.name()))
        elif turn >= 30:
            print('!!! {0}는(은) 늙어 죽었습니다. !!!'.format(dragon.name()))
        break

    # 사용자로부터 용에게 시킬 행동을 입력받는다.
    command = input(mn_action.format(dragon.name()))

    # 각 행동에 따라서 용의 상태를 변화시키고 결과를 출력한다.
    if command == '1':
        if 0 <= dragon.hunger() < 5:
            dragon.change('hunger')
            print('배고픔이 감소했습니다.')
        elif dragon.hunger() < 0:
            print('{}는(은) 배불러서 더 이상 먹을 수 없습니다.'.format(dragon.name()))
    elif command == '2':
        dragon.change('joy')
        if dragon.joy() > 0:
            print('{}는(은) 행복해 보입니다.'.format(dragon.name()))
    elif command == '3':
        if 0 <= dragon.fatigability() < 5:
            dragon.change('fatigability')
            print('피로도가 감소했습니다.')
        elif dragon.fatigability() < 0:
            print('{}는(은) 너무 많이 자서 피곤하지 않습니다.'.format(dragon.name()))
    elif command == '4':
        dragon.change('affection')
        if dragon.affection() > 0:
            print('{}는(은) 사랑에 빠졌습니다.'.format(dragon.name()))
    elif command == '5':
        if 0 <= dragon.hygiene() < 5:
            dragon.change('hygiene')
            print('위생상태가 나빠졌습니다.')
        elif dragon.hygiene() < 0:
            print('{}는(은) 너무 깨끗해서 더 이상 씻을 필요가 없습니다.'.format(
                dragon.name()))
    else:
        print('번호가 잘못 입력되었습니다!!!!!')
        continue

    # 한번 순회할 때마다 용의 상태를 갱신한다.
    dragon.next_turn()
    turn += 1

# !!!!! END of ex12_2.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
