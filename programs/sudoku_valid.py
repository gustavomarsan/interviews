#'''
# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column,
# each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

# Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the
# layout rules described above. Note that the puzzle represented by grid does not have to be solvable.

# Understanding:
# - Is the grid full?
#  No, there can be empty spaces that have None.
# - You do not have to solve, just check if the non-empty spaces are correct acording to sudoku rules.


def sudoku_valid(grid: list[list[int]]) -> bool:
    set_values = set()
    for l in range(9):  # l = line, c = column
        for c in range(9):
            if grid[l][c]:
                if grid[l][c] in set_values:
                    return False
                else:
                    set_values.add(grid[l][c])
        set_values.clear()

    for c in range(9):  # l = line, c = column
        for l in range(9):
            if grid[l][c]:
                if grid[l][c] in set_values:
                    return False
                else:
                    set_values.add(grid[l][c])
        set_values.clear()

    for sqrcol in range(0, 9, 3):
        for sqrline in range(0, 9, 3):
            for c in range(3):
                for l in range(3):
                    if grid[l + sqrline][c + sqrcol]:
                        if grid[l + sqrline][c + sqrcol] in set_values:
                            return False
                        else:
                            set_values.add(grid[l + sqrline][c + sqrcol])
            set_values.clear()
    return True


grid = [
    [None, 1, 5, None, None, None, None, None, None],
    [None, None, None, None, 2, None, None, None, 6],
    [None, None, None, None, None, None, None, None, None],
    [None, 2, 7, 3, 5, 9, None, 6, 4],
    [None, 4, None, None, 1, 8, None, 5, None],
    [None, 9, 1, 4, 6, 2, None, 7, 3],
    [None, 7, None, None, None, 5, None, None, 9],
    [3, None, 6, 8, None, 1, None, 4, None],
    [None, None, 4, None, 3, None, None, None, None],
]


print(sudoku_valid(grid))
