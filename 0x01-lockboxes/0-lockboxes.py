#!/usr/bin/python3
"""
This module contains a function to determine if all boxes can be unlocked.
"""

from collections import deque
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (List[List[int]]): A list where each element is a list of keys av
        ailable in that box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    if n == 0:
        return False

    # Initialize BFS
    visited = [False] * n
    queue = deque([0])
    visited[0] = True

    while queue:
        box_index = queue.popleft()

        # Access keys from the current box
        for key in boxes[box_index]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    # Check if all boxes have been visited
    return all(visited)
