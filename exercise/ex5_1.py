#!/usr/bin/env python
"""This file is provided for educational purpose and distributed for class use.
Copyright (c) by Jinsoo Park, Seoul National University. All rights reserved.

File name.....: ex5_1.py
Description...: Sample solution for exercise 5-1.
                This program demonstrates how to use simple arithmetic
                operations to calculate food tax, service charge, and total
                price of food.
"""
__author__ = 'Jinsoo Park'
__version__ = '0.1'
__email__ = 'snu.python@gmail.com'


meal = 137.50
tax_rate = 8.875 / 100               # 또는 tax_rate = 0.08875
tip = 15 / 100                       # 또는 tip = 0.15


meal = meal + (meal * tax_rate)      # 또는 meal += meal * tax
total = meal + (meal * tip)

print('{}'.format(round(total, 2)))  # 또는 print('{:.2f}'.format(total))
# print(f'{round(total, 2)}')          # 또는 print(f'{total:.2f}')

# !!!!! END of ex5_1.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
