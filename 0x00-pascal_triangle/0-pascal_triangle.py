#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""

def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's triangle of n"""
    if n <= 0:
        return []

    pascal = []

    for i in range(n):
        # Create a new row with 1 at both ends
        row = [1] * (i + 1)

        # Calculate the inner elements of the row
        for j in range(1, i):
            row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

        pascal.append(row)

    return pascal

# Example usage
if __name__ == "__main__":
    print(pascal_triangle(5))
