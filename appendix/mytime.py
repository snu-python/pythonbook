#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: mytime.py
Description...: This module demonstrates the concept of Python 'class' that
                handles clock times. It provides various military and
                conventional time format (12 hours) operations and several
                time-related computations.
Dependencies..: None
"""

__author__ = 'Jinsoo Park'
__copyright__ = 'Copyright (c) 2019 Jinsoo Park, Seoul National University'
__version__ = '0.2'
__email__ = 'snu.python@gmail.com'


class SimpleTime:
    """Represents a simple time

    Attributes.: hour, minute, second
    Methods....: seconds(), ==, !=
    Usages.....:
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

    # --- 초기화 매소드 -------------------------------------------------------- #
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes hour, minute, and second.

        hour...: int hours
        minute.: int minutes
        second.: int seconds
        Usage..:
            >>> t = SimpleTime(1, 25, 57)
            >>> t = SimpleTime(hour=1, minute=30, second=8)
            >>> t = SimpleTime(minute = 3)
        """

        self.hour = hour                # 인스턴스 속성 hour를 초기화한다.
        self.minute = minute            # 인스턴스 속성 minute을 초기화한다.
        self.second = second            # 인스턴스 속성 second를 초기화한다.

    # --- 일반 메소드 ---------------------------------------------------------- #
    def seconds(self):
        """Returns the total number of seconds of the Time.

        Return...: int seconds (time is converted to seconds)
        Usage....:
            >>> t = SimpleTime(1, 25, 57)
            >>> t.seconds()
            5157
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    # --- 특수 메소드 ---------------------------------------------------------- #
    def __repr__(self):
        """Returns representation form of the Time."""
        return ('{0.__class__.__name__}'
                '<{0.hour!r}:{0.minute!r}:{0.second!r}>').format(self)

    def __str__(self):
        """Returns string form of the Time."""
        return '{0.hour!s}:{0.minute!s}:{0.second!s}'.format(self)

    def __eq__(self, other):
        """Returns True if both times are the same."""
        return self.seconds() == other.seconds()

# ===== End of SimpleTime class ============================================= #

class Time(SimpleTime):
    """Represents time in military format, and demonstrates how to use
    properties (@property decorator) to control class member access.

    Attributes.:
        hour, minute, second :
            now they have PRIVATE ATTRIBUTES __hour, __minute, __second
            where the data is actually held by using a decorator @property;
            so that their data are now properly validated.
        seconds :
            SimpleTime.seconds() method returns a single integer, so from
            the user's point of view, it could be treated as a data attribute;
            so a decorator @property is used to create 'read-only' attribute
            with only a 'getter', hence this 'seconds' attribute cannot be
            directly written to or deleted as if PRIVATE.

    Methods.....: ==, !=, >, >=, <, <=, +, -
    Usages......:
        Validation for hour, minute, second is implemented.
        >>> t = SimpleTime(24, -10, -123456)
        >>> t
        SimpleTime<24:-10:-123456>
        >>> t = Time(24, 10, 59)
        Traceback (most recent call last):
        ...
        AssertionError: <hour>는 0-23 사이의 정수여야 합니다.

        All the comparison operators are implemented (i.e., <, <=, >, >=),
        in addition to ==, !=
        >>> t1 = Time(0, 25, 59)
        >>> t2 = Time(hour = 1)
        >>> t1 > t2
        False
        >>> t1 <= t2
        True

        +, - operators are implemented.
        >>> t1 = Time(1, 20, 30)
        >>> t2 = Time(23, 20, 30)
        >>> t1 + t2
        Time<0:41:0>
        >>> t1 = Time(minute = 25)
        >>> t2 = Time(2, 30, 27)
        >>> t1 += t2
        >>> t1
        Time<2:55:27>
        >>> t1 = Time(1, 20, 30)
        >>> t2 = Time(2, 30, 27)
        >>> t1 - t2
        Time<1:9:57>
        >>> t1 = Time(hour = 3, minute = 25)
        >>> t2 = Time(1, 25, 59)
        >>> t2 -= t1
        >>> t2
        Time<1:59:1>
    """

    # --- 초기화 메소드 -------------------------------------------------------- #
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes hour, minute, and second."""

        # Even though it will call SimpleTime class, when it initializes
        # with 'self.hour', 'self.minute', 'self.second', it will call
        # the Time class's 'hour', 'minute', and 'second' property's
        # setters and subsequently their data are validated.
        super().__init__(hour, minute, second)

    # --- 데코레이터 ----------------------------------------------------------- #
    @property
    def seconds(self):
        """Returns the total number of seconds of the Time.

        Python programmers normally use properties rather than the explicit
        getters and setters (e.g., getSeconds() and setSeconds() that are
        commonly used in other object-oriented languages. This is because it
        is so easy to change a data attribute into a property
        without affecting the use of the class.

        Since only getter is provided, 'seconds' is read-only. The code for
        this 'seconds' property is the same as for the 'SimpleTime.seconds()'
        method. The only difference is that it now provides __seconds attribute
        that behaviors like PRIVATE data attribute member.

        Usage...:
            >>> t = SimpleTime(1, -25, 57)  # does not make sense
            >>> t.seconds()
            2157
            >>> t = Time(1, -25, 57)
            Traceback (most recent call last):
            ...
            AssertionError: <minute>은 0-59 사이의 정수여야 합니다.
            >>> t = Time(1, 25, 57)
            >>> t.seconds       # now it is 'seconds', not 'seconds()
            5157
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        self.__seconds = seconds
        return self.__seconds

    @property
    def hour(self):
        """Getter that returns hours in Time.

        Usage...:
            >>> t = Time(24, 10, 13)
            Traceback (most recent call last):
            ...
            AssertionError: <hour>는 0-23 사이의 정수여야 합니다.
            >>> t = Time(23, 10, 13)
            >>> t
            Time<23:10:13>
        """
        return self.__hour

    @hour.setter
    def hour(self, hour):
        """Setter that validates whether 'hour' is  a proper representation,
        and stores hours in the private data attribute __hour.
        """
        assert hour >= 0 and hour < 24, '<hour>는 0-23 사이의 정수여야 합니다.'
        self.__hour = hour

    @property
    def minute(self):
        """Getter that returns minutes in Time.

        Usage...:
            >>> t = Time(minute = 75)
            Traceback (most recent call last):
            ...
            AssertionError: <minute>은 0-59 사이의 정수여야 합니다.
            >>> t = Time(minute = 55)
            >>> t
            Time<0:55:0>
        """
        return self.__minute

    @minute.setter
    def minute(self, minute):
        """Setter that validates whether 'minute' is a proper representation,
        and stores minutes in the private data attribute __minute.
        """
        assert minute >= 0 and minute < 60, '<minute>은 0-59 사이의 정수여야 합니다.'
        self.__minute = minute

    @property
    def second(self):
        """Getter that returns seconds in Time.

        Usage...:
            >>> t = Time()
            >>> t.second = -27
            Traceback (most recent call last):
            ...
            AssertionError: <second>은 0-59 사이의 정수여야 합니다.
            >>> t.second = 27
            >>> t
            Time<0:0:27>
        """
        return self.__second

    @second.setter
    def second(self, second):
        """Setter that validates whether 'second' is a proper representation,
        and stores seconds in the private data attribute __second.
        """
        assert second >= 0 and second < 60, '<second>은 0-59 사이의 정수여야 합니다.'
        self.__second = second

    # --- 내부 조작 메소드 ------------------------------------------------------ #
    def __add_time(self, other):
        """Adds two time objects.

        other..: Time object
        Return.: Time object

        [Caution] This method is intended as non-public, so users should not
        call this method because it is subject to change without notice.
        """
        total_seconds = self.seconds + other.seconds
        return self.__convert_seconds_to_time(total_seconds)

    def __subtract_time(self, other):
        """Subtract this Time object from the other Time object.

        other..: Time object
        Return.: Time object

        [Caution] This method is intended as non-public, so users should not
        call this method because it is subject to change without notice.
        """
        total_seconds = self.seconds - other.seconds
        return self.__convert_seconds_to_time(total_seconds)

    def __convert_seconds_to_time(self, seconds):
        """Converts seconds to Time object.

        seconds.: int seconds
        Return..: Time object

        [Caution] This method is intended as non-public, so users should not
        call this method because it is subject to change without notice.
        """
        converted_seconds = self.__getseconds_for_oneday(abs(seconds))
        minutes, second = divmod(converted_seconds, 60)
        hour, minute = divmod(minutes, 60)
        return self.__class__(hour, minute, second)

    def __getseconds_for_oneday(self, seconds):
        """Return the remaining seconds if the number (seconds) is more than
        one day. One day is 86399 seconds.

        seconds.: int seconds
        Return..: int seconds

        [Caution] This method is intended as non-public, so users should not
        call this method because it is subject to change without notice.
        """
        if seconds >= 86400:  # one day is 86400 seconds
            seconds %= 86400
        return seconds

    # --- 특수 메소드 ---------------------------------------------------------- #
    # 비교 연산자 -------------------------------------------------------------- #
    def __eq__(self, other):
        """Returns True if both times are the same."""

        # This special method must be overridden because SimpleTime's
        # 'seconds()' method is now re-written as a getter property in
        # Time class
        return self.seconds == other.seconds  # let Python handle TypeError

    def __lt__(self, other):
        """Returns True if this time is less than the other time."""
        return self.seconds < other.seconds  # let Python handle TypeError

    def __le__(self, other):
        """Returns True if this time is less than or equal to the other time."""
        return self.seconds <= other.seconds  # let Python handle TypeError

    def __gt__(self, other):
        """Returns True if this time is greater than the other time."""
        return self.seconds > other.seconds  # let Python handle TypeError

    def __ge__(self, other):
        """Returns True if this time is greater than or equal to the other time."""
        return self.seconds >= other.seconds  # let Python handle TypeError

    # 산술 연산자 -------------------------------------------------------------- #
    def __add__(self, other):
        """Returns sum of two Time objects.

        Usage...:
            >>> t1 = Time(1, 20, 30)
            >>> t2 = Time(23, 20, 30)
            >>> t1 + t2
            Time<0:41:0>
        """
        if isinstance(other, self.__class__):
            return self.__add_time(other)
        else:
            raise TypeError("'{}'는 '{}'의 인스턴스이며 'Time' 클래스의 유효한 객체가 "
                '아닙니다.'.format(other, other.__class__.__name__))

    # [FYI] The following method could be commented out to allow the data type
    # that implements arithmetic operators to handle this.
    def __radd__(self, other):
        """Returns sum of two Time objects.

        Usage...:
            >>> t1 = Time(2, 30, 27)
            >>> 60 + t1.seconds
            9087
            >>> t1._convert_seconds_to_time(9087)
            Time<2:31:27>
            >>> Time._convert_seconds_to_time(t1, 60 + t1.seconds)
            Time<2:31:27>
        """
        return self.__add__(other)

    # [FYI] Since __iadd__ behaviors exactly like __add__, the following method
    # could be commented out.
    def __iadd__(self, other):
        """Returns sum of two Time objects.

        Usage...:
            >>> t1 = Time(minute=25)
            >>> t1 += Time(2, 30, 27)
            >>> t1
            Time<2:55:27>
        """
        if isinstance(other, self.__class__):
            return self.__add_time(other)
        else:
            raise TypeError("'{}'는 '{}'의 인스턴스이며 'Time' 클래스의 유효한 객체가 "
                '아닙니다.'.format(other, other.__class__.__name__))

    def __sub__(self, other):
        """Returns difference of two Time objects.

        Usage...:
            >>> t1 = Time(1, 20, 30)
            >>> t2 = Time(23, 20, 30)
            >>> t1 - t2
            Time<22:0:0>
        """
        if isinstance(other, self.__class__):
            return self.__subtract_time(other)
        else:
            raise TypeError("'{}'는 '{}'의 인스턴스이며 'Time' 클래스의 유효한 객체가 "
                '아닙니다.'.format(other, other.__class__.__name__))

    # [FYI] The following method could be commented out to allow the data type
    # that implements arithmetic operators to handle this.
    def __rsub__(self, other):
        """Returns difference of two Time objects.

        Usage...:
            >>> t1 = Time(2, 30, 27)
            >>> 60 - t1.seconds
            -8967
            >>> t1.__convert_seconds_to_time(-8967)
            Time<2:29:27>
            >>> Time.__convert_seconds_to_time(t1, 60 - t1.seconds)
            Time<2:29:27>
        """
        return self.__sub__(other)

    # [FYI] Since __isub__ behaviors exactly like __sub__, the following method
    # could be commented out.
    def __isub__(self, other):
        """Returns difference of two Time objects.

        Usage...:
            >>> t1 = Time(minute=25)
            >>> t1 -= Time(2, 30, 27)
            >>> t1
            Time<2:5:27>
        """
        if isinstance(other, self.__class__):
            return self.__subtract_time(other)
        else:
            raise TypeError("'{}'는 '{}'의 인스턴스이며 'Time' 클래스의 유효한 객체가 "
                '아닙니다.'.format(other, other.__class__.__name__))

# ===== End of Time class =================================================== #

class Clock(Time):
    """Represents time in clock format (e.g., 1:35PM, 11:37AM).

    Attributes.: none
    Methods....: getclockhour()
    Usage......:
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
        """Initializes hour, minute, and second."""

        super().__init__(hour, minute, second)

    # --- 내부 조작 메소드 ------------------------------------------------------ #
    def __getclockhour(self):
        """Returns clock time for PM."""
        return self.hour if self.hour <= 12 else self.hour % 12

    # --- 특수 메소드 ---------------------------------------------------------- #
    def __repr__(self):
        """Returns representation form of the Time in Clock format."""
        if self.hour < 12:
            return ('{0.__class__.__name__}'
                '<{0.hour!r}:{0.minute!r}:{0.second!r}>AM').format(self)
        else:
            return ('{0.__class__.__name__}'
                '<{1!r}:{0.minute!r}:{0.second!r}>PM').format(self,
                    self.__getclockhour())

    def __str__(self):
        """Returns string form of the Time in Clock format."""
        if self.hour < 12:
            return '{0.hour!s}:{0.minute!s}:{0.second!s}AM'.format(self)
        else:
            return '{1!s}:{0.minute!s}:{0.second!s}PM'.format(self,
                self.__getclockhour())


# ===== End of Clock class ================================================== #

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
