import argparse
from tqdm import tqdm


def is_consistent(grid, row, col, num):
    # check column and row
    for x in range(9):
        if (grid[row][x] == num) or (grid[x][col] == num):
            return False

    # check local square
    sq_col = col - col % 3
    sq_row = row - row % 3
    for i in range(3):
        for j in range(3):
            if grid[sq_row + i][sq_col + j] == num:
                return False

    return True


def solve_sudoku(grid, row, col):
    # Brute force backtracking method.

    N = len(grid)

    # stopping method
    if (row == N - 1) and (col > N - 1):
        return True

    # increment row
    if col == N:
        row += 1
        col = 0

    # increment col if local solution known
    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)

    # iterate options for cell
    for num in range(1, N + 1, 1):

        # if consistent, set cell to num
        if is_consistent(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid, row, col + 1):
                return True

        # otherwise set to 0 and implicitly backtrack
        grid[row][col] = 0
    return False


def solution():
    with open('data/096.txt', 'r') as f:
        grids = [grid.split('\n')[1:10] for grid in f.read().split('Grid')[1:]]
        grids = [[[int(d) for d in c] for c in r] for r in grids]

    total = 0
    for grid in tqdm(grids):
        solve_sudoku(grid, 0, 0)
        dig = 0
        for i in range(3):
            dig += grid[0][i] * 10 ** (2 - i)
        total += dig
    return total


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Problem 96')
    args = parser.parse_args()

    problem = 96
    answer = solution()

    print(f'The answer to problem {problem} is {answer}')
