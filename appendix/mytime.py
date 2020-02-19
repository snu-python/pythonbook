#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: mytime.py
Module name...: 12 - Classes and Objects
Lab...........: Appendix 6
Description...: This module demonstrates the concept of Python 'class' that
                handles clock times. It provides both military and conventional
                time format (12 hours) operations and several time-related
                computations.
Dependencies..: None
"""

__author__ = 'Jinsoo Park'
__copyright__ = 'Copyright (c) 2020 Jinsoo Park, Seoul National University'
__version__ = '0.4'
__email__ = 'jinsoo@snu.ac.kr'


class SimpleTime:
    """아주 간단한 시간 클래스다.

    Attributes:
        hour (int): 시간 중 시를 나타낸다.
        minute (int): 시간 중 분을 나타낸다.
        second (int): 시간 중 초를 나타낸다.

    Methods:
        __init__(self, hour: int, minute: int, second: int) -> None:
        __str__(self) -> str:
        __repr__(self) -> str:
        __eq__(self, other) -> bool:
        seconds(self) -> int:

    To use:
        >>> t1 = SimpleTime(1, 25, 57)
        >>> t1
        SimpleTime<1:25:57>
        >>> print(t1)
        1:25:57
        >>> t1.hour, t1.minute, t1.second
        (1, 25, 57)
        >>> t1.seconds()
        5157
        >>> t2 = SimpleTime(second=30)
        >>> t3 = SimpleTime(0, 0, 30)
        >>> t2 == t3
        True
        >>> t1 == t2
        False
    """

    # --- 초기화 메소드 -------------------------------------------------------- #
    def __init__(self, hour=0, minute=0, second=0):
        """시간의 시, 분, 초를 초기화한다. 기본값은 모두 0이다.

        Args:
            hour (int): 시간 중 0~23 사이의 시
            minute (int): 시간 중 0-59 사이의 분
            second (int): 시간 중 0-59 사의의

        To use:
            >>> t = SimpleTime(1, 25, 57)
            >>> t = SimpleTime(hour=1, minute=30, second=8)
            >>> t = SimpleTime(minute=3)
        """

        self.hour = hour
        self.minute = minute
        self.second = second

    # --- 특수 메소드 --------------------------------------------------------- #
    def __str__(self):
        """시간을 텍스트 형식으로 반환한다.

        Returns:
            str: 텍스트 형식으로 표현한시간
        """
        return f'{self.hour!s}:{self.minute!s}:{self.second!s}'

    def __repr__(self):
        """시간으로 대표 형식으로 출력한다.

        Returns:
            str: 대표 형식으로 표현 시간
        """
        return (f'{self.__class__.__name__}'
                f'<{self.hour!r}:{self.minute!r}:{self.second!r}>')

    def __eq__(self, other):
        """비교하는 시간과 같은 시간이면 참(True)을 반하고 그렇지 않으면 거짓(False)을 반환한다.

        Args:
            other (SimpleTime): 시간 객체

        Returns:
            bool: 두 시간이 같은 시간이면 True 그렇기 않으면 False
        """
        return self.seconds() == other.seconds()

    # --- 일반 메소드 ---------------------------------------------------------- #
    def seconds(self):
        """시간을 초 단위로 환산하 반환한다.

        Returns:
            int: 초 단위로 환산한 시

        To use:
            >>> t = SimpleTime(1, 25, 57)
            >>> t.seconds()
            5157
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

# === END of SimpleTime class ============================================= #

class Time(SimpleTime):
    """24 시간 형식의 시간을 표현하는 클래스다. 데코레이터를 사용하는 방법을 학습하기 위한 목적으로
    만든 클래스다.

    Properties:
        hour (int): 시간 중 0~23 사이의 시를 나타내며 __hour에 직접 접근 못하도록 한다.
        minute (int): 시간 중 0-59 사이의 분을 나타내며 __minute애 직접 접근 못하도록 한다.
        second (int): 시간 중 0-59 사의의 초를 나타내며 __second에 접근 못하도록 한다.
        seconds (int): 읽기 전용(read-only)으로 시간으로 초 단위로 환산한 값을 가지고 있다.

    Methods:
        __init__(self, hour: int, minute: int, second: int) -> None:
        __eq__(self, other: Time) -> bool:
        __lt__(self, other: Time) -> bool:
        __le__(self, other: Time) -> bool:
        __gt__(self, other: Time) -> bool:
        __ge__(self, other: Time) -> bool:
        __add__(self, other: Time) -> Time:
        __radd__(self, other: Time) -> Time:
        __iadd__(self, other: Time) -> Time:
        __sub__(self, other: Time) -> Time:
        __rsub__(self, other: Time) -> Time:
        __isub__(self, other: Time) -> Time:
        __add_time(self, other: Time) -> Time:
        __subtract_time(self, other: Time) -> Time:
        __convert_seconds_to_time(self, seconds: int) -> Time:
        __getseconds_for_oneday(self, seconds: int) -> int

    To use:
        # --- Time 클래스는 SimpleTime 클래스와는 달리 시, 분, 초 단위에 유효한 값만 입력받는다.
        >>> t = SimpleTime(24, -10, -123456)
        >>> t
        SimpleTime<24:-10:-123456>
        >>> t = Time(24, 10, 59)
        Traceback (most recent call last):
        ...
        AssertionError: '시'는 0-23 사이의 정수여야 합니다.

        # --- 비교 연산(==, !=, < <=, >=, >)을 모두 구현했다.
        >>> t1 = Time(0, 25, 59)
        >>> t2 = Time(hour=1)
        >>> t1 > t2
        False
        >>> t1 <= t2
        True

        # --- 더하기(+, +=)와 뺴기(-, -=) 연산을 구현했다.
        >>> t1 = Time(1, 20, 30)
        >>> t2 = Time(23, 20, 30)
        >>> t1 + t2
        Time<0:41:0>
        >>> t1 = Time(minute=25)
        >>> t2 = Time(2, 30, 27)
        >>> t1 += t2
        >>> t1
        Time<2:55:27>
        >>> t1 = Time(1, 20, 30)
        >>> t2 = Time(2, 30, 27)
        >>> t1 - t2
        Time<1:9:57>
        >>> t1 = Time(hour=3, minute=25)
        >>> t2 = Time(1, 25, 59)
        >>> t2 -= t1
        >>> t2
        Time<1:59:1>
    """

    # --- 초기화 메소드 -------------------------------------------------------- #
    def __init__(self, hour=0, minute=0, second=0):
        """시간의 시, 분, 초를 초기화한다. 기본값은 모두 0이다.

        Note:
            super() 함수는 하위 클래스에서 상위 클래스의 메소드를 호출할 때 사용한다. 만약 
            하위 클래스에서 __init__() 메소드를 정의하게 되면, 결과적으로 상위 클래스의 
            __init__() 메소드를 재정의한 것이 된다. 따라서, 더 이상 상위 클래스의 
            __init__() 메소드를 자동으로 호출하지 않기 때문에 명시적으로 super() 함수를 
            사용해서 상위 클래스인 SimpleTime의 __init__() 메소드를 호출해야 한다.
        
        Args:
            hour (int): 시간 중 0~23 사이의 시
            minute (int): 시간 중 0-59 사이의 분
            second (int): 시간 중 0-59 사의의
        """
        super().__init__(hour, minute, second)

    # --- 데코레이터 ---------------------------------------------------------- #
    @property
    def hour(self):
        """시간 중 시를 반환한다.

        Returns:
            int: 시
        """
        return self.__hour

    @hour.setter
    def hour(self, hour):
        """시간 중 시를 설정한다.

        속성 __hour에 시를 할당하기 전에 시가 0~23(둘 다 포함) 사이의 정수인지를 확인한다.

        Args:
            hour (int): 0~23 사이의 시

        Raises:
            AssertionError: 0~23(둘 다 포함) 사이의 정수가 아니면 발생한다.

        To use:
            >>> t = Time(24, 10, 13)
            Traceback (most recent call last):
            ...
            AssertionError: '시'는 0-23 사이의 정수여야 합니다.
            >>> t = Time(23, 10, 13)
            >>> t
            Time<23:10:13>
        """
        assert hour >= 0 and hour < 24, "'시'는 0-23 사이의 정수여야 합니다."
        self.__hour = hour

    @property
    def minute(self):
        """시간 중 분을 반환한다.

        Returns:
            int: 분
        """
        return self.__minute

    @minute.setter
    def minute(self, minute):
        """시간 중 분을 설정한다.

       속성 __minute에 분을 할당하기 전에 분이 0~59(둘 다 포함) 사이의 정수인지를 확인한다.

       Args:
           minute (int): 0~59 사이의 분

       Raises:
           AssertionError: 0~59(둘 다 포함) 사이의 정수가 아니면 발생한다.

       To use:
            >>> t = Time(minute=75)
            Traceback (most recent call last):
            ...
            AssertionError: '분'은 0-59 사이의 정수여야 합니다.
            >>> t = Time(minute=55)
            >>> t
            Time<0:55:0>
        """
        assert minute >= 0 and minute < 60, "'분'은 0-59 사이의 정수여야 합니다."
        self.__minute = minute

    @property
    def second(self):
        """시간 중 초를 반환한다.

        Returns:
            int: 초
        """
        return self.__second

    @second.setter
    def second(self, second):
        """시간 중 분을 설정한다.

        속성 __second에 초를 할당하기 전에 초가 0~59(둘 다 포함) 사이의 정수인지를 확인한다.

        Args:
            second (int): 0~59 사이의 초

        Raises:
            AssertionError: 0~59(둘 다 포함) 사이의 정수가 아니면 발생한다.

        To use:
            >>> t = Time()
            >>> t.second = -27
            Traceback (most recent call last):
            ...
            AssertionError: '초' 0-59 사이의 정수여야 합니다.
            >>> t.second = 27
            >>> t
            Time<0:0:27>
        """
        assert second >= 0 and second < 60, "'초'는 0-59 사이의 정수여야 합니다."
        self.__second = second

    @property
    def seconds(self):
        """시간을 초 단위로 환산해서 반환한다.

        Note:
        이 메소드의 데코레이터로 @property만 사용하기 때문에 읽기 전용(read-only)이다.
        여기 코드는 SimpleTime의 seconds() 메소드와 같다.

        To Use:
            >>> t = SimpleTime(1, -25, 57)  # This does not make sense.
            >>> t.seconds()
            2157
            >>> t = Time(1, -25, 57)
            Traceback (most recent call last):
            ...
            AssertionError: '분'은 0-59 사이의 정수여야 합니다.
            >>> t = Time(1, 25, 57)
            >>> t.seconds       # Now it is 'seconds', not 'seconds()
            5157
        """
        minutes = self.__hour * 60 + self.__minute
        seconds = minutes * 60 + self.__second
        return seconds

    # --- 특수 메소드 ---------------------------------------------------------- #
    # - 비교 연산자 ------------------------------------------------------------ #
    def __eq__(self, other):
        """비교하는 시간과 같은 시간이면 참(True)을 반환하고 그렇지 않으면 거짓(False)을 반환한다.
        
        Note:
            SimpleTime 클래스의 __eq__() 메소드는 seconds() 매소드를 호출하기 때문에 Time
            클래스에서 seconds를 사용하기 위해 새로 재정의해야 한다.

        Args:
            other (Time): 시간 객체

        Returns:
            bool: 두 시간이 같은 시간이면 True 그렇기 않으면 False
        """
        # TypeError 오류는 파이썬이 처리하도록 한다.
        return self.seconds == other.seconds

    def __lt__(self, other):
        """비교하는 시간보다 빠르면 참(True)을 반환하고 그렇지 않으면 거짓(False)을 반환한다.

        Args:
            other (Time): 시간 객체

        Returns:
            bool: 비교하는 시간보다 빠르면 True 그렇기 않으면 False
        """
        # TypeError 오류는 파이썬이 처리하도록 한다.
        return self.seconds < other.seconds

    def __le__(self, other):
        """비교하는 시간보다 같거나 빠르면 참(True)을 반환하고 그렇지 않으면 거짓(False)을 반환한다.

        Args:
            other (Time): 시간 객체

        Returns:
            bool: 비교하는 시간보다 같거나 빠르면 True 그렇기 않으면 False
        """
        # TypeError 오류는 파이썬이 처리하도록 한다.
        return self.seconds <= other.seconds

    def __gt__(self, other):
        """비교하는 시간보다 늦으면 참(True)을 반환하고 그렇지 않으면 거짓(False)을 반환한다.

        Args:
            other (Time): 시간 객체

        Returns:
            bool: 비교하는 시간보다 늦으면 True 그렇기 않으면 False
        """
        # TypeError 오류는 파이썬이 처리하도록 한다.
        return self.seconds > other.seconds

    def __ge__(self, other):
        """비교하는 시간보다 같거나 늦으면 참(True)을 반환하고 그렇지 않으면 거짓(False)을 반환한다.

        Args:
            other (Time): 시간 객체

        Returns:
            bool: 비교하는 시간보다 같거나 늦으면 True 그렇기 않으면 False
        """
        # TypeError 오류는 파이썬이 처리하도록 한다.
        return self.seconds >= other.seconds

    # - 산술 연산자 ------------------------------------------------------------ #
    def __add__(self, other):
        """자신과 우변의 시간을 합한 시간을 반환하다. 24시간 초과하면 24시간을 초과한 시간만 반환한다.

        Args:
            other (Time): 시간 객체

        Returns:
            Time: 두 시간 객체를 합한 시간

        Raises:
             TypeError: 시간 객체가 아니면 오류가 난다.

        To use:
            >>> t1 = Time(1, 20, 30)
            >>> t2 = Time(23, 20, 30)
            >>> t1 + t2
            Time<0:41:0>
        """
        if isinstance(other, self.__class__):
            return self.__add_time(other)
        else:
            raise TypeError(
                f"'{other}'는 '{other.__class__.__name__}'의 인스턴스며 "
                f"'Time' 클래스의 유효한 객체가 아닙니다.")

    def __radd__(self, other):
        """자신과 좌변의 시간을 합한 시간을 반환한다. 24시간을 초과하면 24시간을 초과한 시간만 반환한다.

        Note:
            좌변의 피연산자로 하여금 우변의 시간을 더하기 하게 하려면 __radd__()는 생략하면 된다.

        Args:
            other (Time): 시간 객체

        Returns:
            Time: 두 시간 객체를 합한 시간

        Raises:
             TypeError: 시간 객체가 아니면 오류가 난다.

        To use:
            >>> t1 = Time(2, 30, 27)
            >>> 60 + t1.seconds
            9087
            >>> t1.__convert_seconds_to_time(9087)
            Time<2:31:27>
            >>> Time.__convert_seconds_to_time(t1, 60 + t1.seconds)
            Time<2:31:27>
        """
        return self.__add__(other)

    def __iadd__(self, other):
        """자신과 우변의 시간을 합한 시간으로 자신의 시간을 갱신한다. 24시간을 초과하면 24시간을
        초과한 시간만 반환한다.

        Note:
            __iadd__()는 __add__()와 같은 연산 논리이기 때문에 생략해도 된다.

        Args:
            other (Time): 시간 객체

        Returns:
            Time: 두 시간 객체를 합한 시간

        Raises:
             TypeError: 시간 객체가 아니면 오류가 난다.

        To use:
            >>> t1 = Time(minute=25)
            >>> t1 += Time(2, 30, 27)
            >>> t1
            Time<2:55:27>
        """
        if isinstance(other, self.__class__):
            return self.__add_time(other)
        else:
            raise TypeError(
                f"'{other}'는 '{other.__class__.__name__}'의 인스턴스며 "
                f"'Time' 클래스의 유효한 객체가 아닙니다.")

    def __sub__(self, other):
        """자신의 시간에서 우변의 시간을 뺀 시간의 절댓값을 반환한다. 24시간을을 초과하면 24시간을
        초과한 시간만 반환한다.

        Args:
            other (Time): 시간 객체

        Returns:
            Time: 두 시간 객체의 차이를 절댓값으로 계산한 시간

        Raises:
             TypeError: 시간 객체가 아니면 오류가 난다.

        To use:
            >>> t1 = Time(1, 20, 30)
            >>> t2 = Time(23, 20, 30)
            >>> t1 - t2
            Time<22:0:0>
        """
        if isinstance(other, self.__class__):
            return self.__subtract_time(other)
        else:
            raise TypeError(
                f"'{other}'는 '{other.__class__.__name__}'의 인스턴스며 "
                f"'Time' 클래스의 유효한 객체가 아닙니다.")

    def __rsub__(self, other):
        """자신의 시간에서 우변의 시간을 뺀 시간의 절댓값을 반환한다. 24시간을 초과하면 24시간을
        초과한 시간만 반환한다.

        Note:
            좌변의 피연산자로 하여금 우변의 시간을 빼기 연산하게 하려면 __rsub__() 생략하면 된다.

        Args:
            other (Time): 시간 객체

        Raises:
             TypeError: 시간 객체가 아니면 오류가 난다.

        To use:
            >>> t1 = Time(2, 30, 27)
            >>> 60 - t1.seconds
            -8967
            >>> t1.__convert_seconds_to_time(-8967)
            Time<2:29:27>
            >>> Time.__convert_seconds_to_time(t1, 60 - t1.seconds)
            Time<2:29:27>
        """
        return self.__sub__(other)

    def __isub__(self, other):
        """자신의 시간에서 우변의 시간을 뺀 시간의 절댓값으로 자신의 시간을 갱신한다. 24시간을 초과하면
        24시간을 초과한 시간만 반환한다.

        Note:
            __isub__()는 __sub__()와 같은 연산 논리이기 때문에 생략해도 된다.

        Args:
            other (Time): 시간 객체

        Raises:
             TypeError: 시간 객체가 아니면 오류가 난다.

        To use:
            >>> t1 = Time(minute=25)
            >>> t1 -= Time(2, 30, 27)
            >>> t1
            Time<2:5:27>
        """
        if isinstance(other, self.__class__):
            return self.__subtract_time(other)
        else:
            raise TypeError(
                f"'{other}'는 '{other.__class__.__name__}'의 인스턴스며 "
                f"'Time' 클래스의 유효한 객체가 아닙니다.")

    # --- 내부 전용 메소드 ------------------------------------------------------ #
    def __add_time(self, other):
        """두 시간 객체의 시간을 합해서 반환하다. 24시간 초과하면 24시간을 초과한 시간만 반환한다.

        Note:
            이 메소드는 내부 전용으로 구현한 비공용(non-public) 메소드라서 언제든지 그 내용과 이름이
            바뀔 수 있다. 따라서 외부에서 이 메소드를 직접 호출해서 사용하는 것을 권장하지 않는다.

        Args:
            other (Time): 시간 객체

        Returns:
            Time: 두 시간 객체를 합한 시간
        """
        total = self.seconds + other.seconds
        return self.__convert_seconds_to_time(total)

    def __subtract_time(self, other):
        """두 시간 객체의 시간 차를 절댓값으로 계산한 시간 객체를 반환하다. 24시간을을 초과하면
        24시간을 초과한 시간만 반환한다.

        Note:
            이 메소드는 내부 전용으로 구현한 비공용(non-public) 메소드라서 언제든지 그 내용과 이름이
            바뀔 수 있다. 따라서 외부에서 이 메소드를 직접 호출해서 사용하는 것을 권장하지 않는다.

        Args:
            other (Time): 시간 객체

        Returns:
            Time: 두 시간 객체의 차이를 양의 값으로 계산한 시간
        """
        difference = abs(self.seconds - other.seconds)
        return self.__convert_seconds_to_time(difference)

    def __convert_seconds_to_time(self, seconds):
        """초를 시간으로 환산한 시간 객체를 반환한다. 이때 24시간을 초과하면 24시간을 초과한 시간만
        환산해서 반환한다.

        Note:
            이 메소드는 내부 전용으로 구현한 비공용(non-public) 메소드라서 언제든지 그 내용과 이름이
            바뀔 수 있다. 따라서 외부에서 이 메소드를 직접 호출해서 사용하는 것을 권장하지 않는다.

        Args:
            seconds (int): 초

        Returns:
            Time: 초를 시간으로 환산한 시간 객체
        """
        converted_seconds = self.__getseconds_for_oneday(seconds)
        minutes, second = divmod(converted_seconds, 60)
        hour, minute = divmod(minutes, 60)
        return self.__class__(hour, minute, second)

    def __getseconds_for_oneday(self, seconds):
        """초가 24시간을 초과하면 하루를 넘긴 초를 뺀 초를 반환한다. 하루는 86,400초다.

        Note:
            이 메소드는 내부 전용으로 구현한 비공용(non-public) 메소드라서 언제든지 그 내용과 이름이
            바뀔 수 있다. 따라서 외부에서 이 메소드를 직접 호출해서 사용하는 것을 권장하지 않는다.

        Args:
            seconds (int): 초

        Returns:
            int: 하루 단위로 계산한 초
        """
        if seconds >= 86400:  # 하루는 86,400초다.
            seconds %= 86400
        return seconds

# === END of Time class =================================================== #

class Clock(Time):
    """12 시간 형식의 시간을 표현하는 클래스다.

    Methods:
        __init__(self, hour: int, minute: int, second: int) -> None:
        __str__(self) -> str:
        __repr__(self) -> str:
        __clockhour(self) -> int:

    To use:
        >>> t1 = Clock(11, 59, 59)
        >>> t2 = Clock(hour = 13)
        >>> t1
        Clock<11:59:59>AM
        >>> print(t1)
        11:59:59am
        >>> t2
        Clock<1:0:0>PM
        >>> print(t2)
        1:0:0pm
        >>> t1 > t2
        False
        >>> t1 + t2
        Clock<0:59:59>AM
        >>> t1 - t2
        Clock<1:0:1>AM
        >>> t1 -= t2
        >>> t1
        Clock<1:0:1>AM
        >>> t2 += t1
        >>> print(t2)
        2:0:1pm
    """

    # --- 초기화 메소드 -------------------------------------------------------- #
    def __init__(self, hour=0, minute=0, second=0):
        """시간의 시, 분, 초를 초기화한다. 기본값은 모두 0이다.

        Args:
            hour (int): 시간 중 0~23 사이의 시
            minute (int): 시간 중 0-59 사이의 분
            second (int): 시간 중 0-59 사의의
        """
        super().__init__(hour, minute, second)

    # --- 특수 메소드 --------------------------------------------------------- #
    def __str__(self):
        """시간을 12시간 형태로 표현하는 텍스트 형식으로 반환한다.

        Returns:
            str: 텍스트 형식으로 표현한 12시간 형태의 시간
        """
        if self.hour < 12:
            return f'{self.hour!s}:{self.minute!s}:{self.second!s}AM'
        else:
            return f'{self.__getclockhour()!s}:{self.minute!s}:{self.second!s}PM'

    def __repr__(self):
        """시간을 12시간 형태로 표현하는 대표 형식으로 출력한다.

        Returns:
            str: 대표 형식으로 표현한 12시간 형태의 시
        """
        if self.hour < 12:
            return (f'{self.__class__.__name__}'
                    f'<{self.hour!r}:{self.minute!r}:{self.second!r}>AM')
        else:
            return (
                f'{self.__class__.__name__}'
                f'<{self.__getclockhour()!r}:{self.minute!r}:{self.second!r}>PM')

    # --- 내부 전용 메소드 ------------------------------------------------------ #
    def __getclockhour(self):
        """13~23시면 PM을 사용해서 12시간 형태로 표현한다.

        Returns:
            int: 0~12 사이의 시
        """
        return self.hour if self.hour <= 12 else self.hour % 12

# === End of Clock class ================================================== #
# ----- time module Testing ------------------------------------------------- #
def main():
    print('========== SimpleTime Class Demo ==================')
    print('>>> from mytime import SimpleTime')
    print('>>> t1 = SimpleTime(1, 25, 57)')
    t1 = SimpleTime(1, 25, 57)
    print('>>> t1')
    print(repr(t1))
    print('>>> print(t1)')
    print(t1)
    print('>>> t1.hour, t1.minute, t1.second')
    print('(' + str(t1.hour) + ', ' + str(t1.minute) + ', '+ str(t1.second) + ')')
    print('>>> t1.seconds()')
    print(t1.seconds())
    print('>>> t2 = SimpleTime(second=30)')
    t2 = SimpleTime(second=30)
    print('>>> t3 = SimpleTime(0, 0, 30)')
    t3 = SimpleTime(0, 0, 30)
    print('>>> t2 == t3')
    print(t2 == t3)
    print('>>> t1 == t2')
    print(t1 == t2)

    print()
    print('========== Time Class Demo =================')
    print('>>> from mytime import SimpleTime, Time')
    print('>>> t = SimpleTime(24, -10, -123456)')
    t = SimpleTime(24, -10, -123456)
    print('>>> t')
    print(repr(t))
    print('>>> t = Time(24, 10, 59)')
    print('Traceback (most recent call last):')
    print('...')
    print('AssertionError: <hour>는 0-23 사이의 정수여야 합니다.')
    # try:
    #    t = Time(24, 10, 59)
    # except AssertionError as e:
    #    print(('The above code raises AssertionError exception with '
    #        'the following message:'))
    #    print(e)
    print(
        '----- All the comparison operators are implemented (==, !=, <, <=, >, >=) -----')
    print('>>> t1 = Time(0, 25, 59)')
    t1 = Time(0, 25, 59)
    print('>>> t2 = Time(hour = 1)')
    t2 = Time(hour=1)
    print('>>> t1 > t2')
    print(t1 > t2)
    print('>>> t1 <= t2')
    print(t1 <= t2)
    print('----- +, - operators are implemented -----')
    print('>>> t1 = Time(1, 20, 30)')
    t1 = Time(1, 20, 30)
    print('>>> t2 = Time(23, 20, 30)')
    t2 = Time(23, 20, 30)
    print('>>> t1 + t2')
    print(repr(t1 + t2))
    print('>>> t1 = Time(minute = 25)')
    t1 = Time(minute=25)
    print('>>> t2 = Time(2, 30, 27)')
    t2 = Time(2, 30, 27)
    print('>>> t1 += t2')
    t1 += t2
    print('>>> t1')
    print(repr(t1))
    print('>>> t1 = Time(1, 20, 30)')
    t1 = Time(1, 20, 30)
    print('>>> t2 = Time(2, 30, 27)')
    t2 = Time(2, 30, 27)
    print('>>> t1 - t2')
    print(repr((t1 - t2)))
    print('>>> t1 = Time(hour = 3, minute = 25)')
    t1 = Time(hour=3, minute=25)
    print('>>> t2 = Time(1, 25, 59)')
    t2 = Time(1, 25, 59)
    print('>>> t2 -= t1')
    t2 -= t1
    print('>>> t2')
    print(repr(t2))
    print('>>> t2 - 57')
    print('Traceback (most recent call last):')
    print('...')
    print("TypeError: '57'는 'int'의 인스턴스이며 'Time' 클래스의 유효한 객체가 아닙니다.")
    # try:
    #    t2 - 57
    # except TypeError as e:
    #    print(('The above code raises TypeError exception with '
    #        'the following message:'))
    #    print(e)
    print()
    print('========== Clock Class Demo ==================')
    print('>>> t1 = Clock(11, 59, 59)')
    t1 = Clock(11, 59, 59)
    print('>>> t2 = Clock(hour = 13)')
    t2 = Clock(hour = 13)
    print('>>> t1')
    print(repr(t1))
    print('>>> print(t1)')
    print(t1)
    print('>>> t2')
    print(repr(t2))
    print('>>> print(t2)')
    print(t2)
    print('>>> t1 > t2')
    print(repr(t1 > t2))
    print('>>> t1 + t2')
    print(repr(t1 + t2))
    print('>>> t1 - t2')
    print(repr(t1 - t2))
    print('>>> t1 -= t2')
    t1 -= t2
    print('>>> t1')
    print(repr(t1))
    print('>>> t2 += t1')
    t2 += t1
    print('>>> print(t2)')
    print(t2)

# ----- Testing Time module ---------------------------------------------------
# 이 파일을 import하는 대신에 cmd> 에서 cmd> python functions.py처럼 직접 실행할 경우 수행됨
if __name__ == '__main__':
    main()

# !!!!! END OF mytime 모듈 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
