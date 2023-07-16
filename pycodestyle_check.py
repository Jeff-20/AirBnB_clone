#!/usr/bin/python3

"""This module is meant to test pycodestyle and
   see if its checks pass
"""


def print_int():
    """prints 5 integers from 0 to 4 to the STDOUT"""
    for i in range(5):
        print(i)


if __name__ == '__main__':
    print_int()
