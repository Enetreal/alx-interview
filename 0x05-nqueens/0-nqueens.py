#!/usr/bin/python3
"""
N Queens placement on NxN chessboard
"""

import sys


def generate_solutions(row, n):
    """
    Generate all solutions for placing N Queens on an NxN chessboard.
    
    Args:
        row (int): The current row to place the queen.
        n (int): Size of the chessboard (N x N).
        
    Returns:
        list: A list of lists, each inner list representing a valid solution with queen positions.
    """
    if row == n:
        return [[]]

    prev_solution = generate_solutions(row + 1, n)
    solutions = []
    for queen in range(n):
        solutions.extend(place_queen(queen, row, prev_solution))
    return solutions


def place_queen(queen, row, prev_solution):
    """
    Place a queen in the current row and check for safe positions.
    
    Args:
        queen (int): Column where the queen is to be placed.
        row (int): Current row to place the queen.
        prev_solution (list): List of previous solutions.
        
    Returns:
        list: List of lists, each representing a safe position to place the queen.
    """
    safe_positions = []
    for solution in prev_solution:
        if is_safe(queen, row, solution):
            safe_positions.append(solution + [queen])
    return safe_positions


def is_safe(queen, row, solution):
    """
    Check if placing a queen at (row, queen) is safe.
    
    Args:
        queen (int): Column where the queen is to be placed.
        row (int): Current row to place the queen.
        solution (list): List representing the current solution.
        
    Returns:
        bool: True if placing the queen is safe, False otherwise.
    """
    for r, col in enumerate(solution):
        if col == queen or abs(row - r) == abs(queen - col):
            return False
    return True


def init():
    """
    Initialize the size of the chessboard from command-line arguments.
    
    Returns:
        int: Size of the chessboard (N x N).
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens.py N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def n_queens():
    """
    Solve the N Queens problem and print all solutions.
    """
    n = init()
    solutions = generate_solutions(0, n)
    
    for solution in solutions:
        print([[r, col] for r, col in enumerate(solution)])


if __name__ == '__main__':
    n_queens()
