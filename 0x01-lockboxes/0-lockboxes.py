#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list of lists): A list where each sublist contains keys to other
        boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    # Initialize visited set and queue
    visited = set()
    queue = [0]  # Start with the first box

    while queue:
        box = queue.pop(0)
        if box not in visited:
            visited.add(box)
            # Add all keys (boxes) we can reach from the current box
            for key in boxes[box]:
                if key < len(boxes) and key not in visited:
                    queue.append(key)

    # Check if we visited all boxes
    return len(visited) == len(boxes)
