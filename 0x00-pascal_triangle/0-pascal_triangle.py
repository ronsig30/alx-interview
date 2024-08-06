#!/usr/bin/python3
"""
This module contains a function to generate Pascal's Triangle.
"""

from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    """
    Generate Pascal's Triangle of height n.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        List[List[int]]: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
