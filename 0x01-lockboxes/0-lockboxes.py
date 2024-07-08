#!/usr/bin/python3
"""
code to lockboxes opening problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes) - 1):
        b_checked = False
        for idx in range(len(boxes)):
            b_checked = k in boxes[idx] and k != idx
            if b_checked:
                break
        if b_checked is False:
            return b_checked
    return True
