#!/usr/bin/python3
"""
N Queens Challenge
"""

import sys


def is_safe(row, col, placed_queens):
    """Check if placing a queen at (row, col) is safe"""
    for r, c in placed_queens:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


def solve_nqueens(n):
    """Solve the N Queens problem and return all solutions"""
    solutions = []
    placed_queens = []

    def backtrack(row):
        """Backtracking function to place queens recursively"""
        if row == n:
            solutions.append(placed_queens[:])
            return
        for col in range(n):
            if is_safe(row, col, placed_queens):
                placed_queens.append((row, col))
                backtrack(row + 1)
                placed_queens.pop()

    backtrack(0)
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens.py N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solve_nqueens(n)

    for solution in solutions:
        print(solution)
        