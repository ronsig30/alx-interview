def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of int): A 2D grid where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Check for adjacent land cells to subtract shared sides
                if row > 0 and grid[row - 1][col] == 1:  # Up
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:  # Left
                    perimeter -= 2

    return perimeter
