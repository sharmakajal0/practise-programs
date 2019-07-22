#!/usr/bin/env python

'''Module for square root'''

from math import sqrt

def square_root(int_num):

    '''Function definition to print root of the given number'''
    print(sqrt(int_num))
    print(int(sqrt(int_num)))

TEST_CASES = int(input())
while TEST_CASES > 0:
    TEST_CASES -= 1
    TEST_INTEGER = int(input())
    square_root(TEST_INTEGER)
