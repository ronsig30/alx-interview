#!/usr/bin/python3
"""
This module provides a function to calculate the minimum number of operations
needed to achieve exactly n 'H' characters in a file using "Copy All" and "Past
e" operations.
"""


def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations needed to result in exactly n 'H'
    characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed, or 0 if it's impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
