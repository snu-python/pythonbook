#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: lab10_8.py
Description...: Sample solution for Lab 10-8.
                This program demonstrates how to use import, import ... as,
                and from ... import statements to import modules and
                functions from a module.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


import math                         # import로 모듈을 불러온다.
print(math.exp(10))

import math as m                    # import ... as문으로 모듈을 불러온다.
print(m.exp(10))

from math import exp                # from ... import문으로 함수를 불러온다.
print(exp(10))

# !!!!! END of lab10_8.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
