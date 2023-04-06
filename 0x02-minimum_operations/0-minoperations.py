#!/usr/bin/python3
"""
calculates the fewest number of operations
"""


def minOperations(n):
    """
    now return
    """
    a = 0
    b = 2
    while n > 1:
        while n % b == 0:
            a += b
            n = n / b
        b += 1
    return a
