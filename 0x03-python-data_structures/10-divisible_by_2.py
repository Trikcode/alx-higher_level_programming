#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [not x & 1 for x in my_list]
