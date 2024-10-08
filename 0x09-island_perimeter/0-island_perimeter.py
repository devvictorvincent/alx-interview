#!/usr/bin/python3
"""
Calculates the perimeter of an island
described in grid
"""


def island_perimeter(grid):
    """
    Return the perimiter of an island.
    The grid represents water by 0 and land by 1.
    """
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2
    return perimeter
