"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ch12.py
Description...: Sample solution for Real Python of Chapter 12.
                This program demonstrates how to define and use a custom class.
"""
__author__ = 'Jinsoo Park'
__credits__ = '이재환'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


import random                           # 게임을 무작위로 진행하기 위한 모듈
import time                             # 일시 정지를 위해 필요한 모듈

# ----- Player 클래스 정의 ----------------------------------------------------- #
class Player:
    """가위, 바위, 보 게임을 하는 선수 클래스다.

    속성.: cards
    메소드: name(). energy(), status(), pick(), lose()
    """

    cards = '가위', '바위', '보'     # 클래스 속성 : '가위', '바위', '보'를 튜플로 생성한다.

    # --- 초기화 메소드 -------------------------------------------------------- #
    def __init__(self, name, energy):
        """선수의 이름과 에너지 레벨을 초기화하는 메소드다.

        name...: 선수 이름(문자열)
        energy.: 에너지 레벨(정수)
        Returns: None
        """
        self.__name = name              # 인스턴스 속성 : 선수의 이름을 초기화한다.
        self.__energy = energy          # 인스턴스 속성 : 선수의 에너지를 초기화한다.

    # --- 접근자 메소드 -------------------------------------------------------- #
    def name(self):
        """선수의 이름을 반환하는 메소드다.

        Returns: 선수 이름(문자열형)
        """
        return self.__name

    # --- 일반 메소드 --------------------------------------------------------- #
    def energy(self):
        """에너지 레벨을 반환하는 메소드다.

        Returns: 에너지 레벨(정수)
        """
        return self.__energy

    def status(self):
        """선수의 상태를 출력하는 메소드다.

        Returns: None
        """
        print('{}의 남은 에너지 : {}'.format(self.__name, self.__energy))

    def pick(self):
        """가위, 바위, 보 중 임의로 하나를 이다.선택해서 반환하는 메소드다.

        Returns: 임의로 선택된 '가위', '바위', '보' (문자열)
        """
        return random.choice(Player.cards)

    def lose(self):
        """패배시 남은 에너지 하나를 차감하는 메소드다.

        Returns: None
        """
        self.__energy -= 1

        # 남은 에너지가 0보다 작아지지 않게 처리한다.
        self._energy = self.__energy if self.__energy > 0 else 0

# ----- play() 함수 정의 ------------------------------------------------------ #
# 두 선수가 낸 가위, 바위, 보의 결과를 판정하는 일은 반복해서 사용한다.
# 따라서 이를 판정하는 코드를 함수로 처리하면 편리하게 사용할 수 있다
def play(pick1, pick2):
    """가위, 바위, 보 승부의 결과를 알려주는 함수다.

    pick1..: 첫 번째 선수가 낸 가위, 바위, 보 중 하나를 받는 문자열
    pick2..: 두 번째 선수가 낸 가위, 바위, 보 중 하나를 받는 문자열
    Returns: 0 => 무승부(정수)
             1 => 첫 번째 선수 승리(정수)
             2 => 두 번째 선수 승리(정수)
    """
    to_number = {'가위': -1, '바위': 0, '보': 1}
    pick1 = to_number[pick1]
    pick2 = to_number[pick2]

    if pick1 == pick2:
        return 0
    elif pick1 * pick2 == 0:
        return 1 if pick1 > pick2 else 2
    else:
        return 1 if pick1 < pick2 else 2


# ----- 게임 시작 ------------------------------------------------------------- #
# '네오'와 '무지'라는 이름의 선수를 생성해서, 두 선수가 각각 세 개의 에너지를 가지고 게임을 시작한다.
# 한 명이 승리할 때까지 게임을 계속한다.

player1 = Player('네오', 3)                      # 에너지 세 개를 가진 네오 선수
player2 = Player('무지', 3)                      # 에너지 세 개를 가진 네오 선수

player1.status()
player2.status()

count = 0                                       # 게임 횟수를 기록하는 변수를 초기화한다.

# 선수 둘 중 한 명의 에너지가 0이 아니라면 계속 반복 실행한다.
while player1.energy() * player2.energy() != 0:
    count += 1
    print('[ {}회차 게임 ]'.format(count))        # 게임 횟수 정보를 출력한다

    # 두 선수가 각각 임의로 가위, 바위, 보를 선택한다.
    pick1, pick2 = player1.pick(), player2.pick()

    # 두 선수의 이름, 남은 에너지 레벨, 선택한 공격 카드를 출력한다.
    print('| {0}({1})=>{2:2} vs {5:2}<={3}({4}) |'.format(
        player1.name(), player1.energy(), pick1,
        player2.name(), player2.energy(), pick2))

    # 승리한 선수를 판정한다.
    winner = play(pick1, pick2)
    if winner == 1:
        player2.lose()
        print('> {}의 승리!'.format(player1.name()))
    elif winner == 2:
        player1.lose()
        print('> {}의 승리!'.format(player2.name()))
    else:
        print('> 무승부!')

    time.sleep(2)                               # 한 게임 후 2초간 일시 정지한다.
    print()                                     # 빈 줄을 출력한다.

if player1.energy() == 0:
    print('!!! {}회의 승부 끝에 {}의 승리 !!!'.format(count, player2.name()))
else:
    print('!!! {}회의 승부 끝에 {}의 승리 !!!'.format(count, player1.name()))

# !!!!! END of ch12.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!