#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
to meet a given amount total"""

def make_change(coins, total):
    """Calculate the minimum number of coins required to make the total amount.

    Args:
        coins (list): List of coin denominations.
        total (int): The total amount of change needed.

    Returns:
        int: The fewest number of coins needed, or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins = sorted(coins, reverse=True)
    count = 0

    for coin in coins:
        while total >= coin:
            count += 1
            total -= coin

    return count if total == 0 else -1
