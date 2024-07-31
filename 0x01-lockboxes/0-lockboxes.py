#!/usr/bin/python3

def canUnlockAll(boxes):
    from collections import deque

    # Initialize a queue for BFS and a set for visited boxes
    queue = deque([0])
    visited = set([0])
    
    # Perform BFS
    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                visited.add(key)
                queue.append(key)
    
    # Check if all boxes have been visited
    return len(visited) == len(boxes)
