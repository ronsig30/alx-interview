#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """Check if a queen can be placed on board at row, col."""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, n, solutions):
    """Use backtracking to solve the N queens problem."""
    if col == n:
        solutions.append([[i, board[i].index(1)] for i in range(n)])
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0  # Backtrack

    return res


def solve_nqueens(n):
    """Solve the N queens problem and print all solutions."""
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
