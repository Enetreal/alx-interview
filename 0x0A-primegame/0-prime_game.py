#!/usr/bin/python3
"""
Prime Game
"""

def generate_primes(limit):
    """Generate a list of prime numbers up to a given limit.
    
    Args:
        limit (int): The upper boundary of the range (inclusive).
    
    Returns:
        List[int]: A list of prime numbers up to the limit.
    """
    if limit < 2:
        return []
    
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    primes = []
    
    for num in range(2, limit + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    
    return primes

def is_winner(num_rounds, rounds):
    """
    Determines the winner of the Prime Game.
    
    Args:
        num_rounds (int): Number of rounds in the game.
        rounds (List[int]): A list of upper limits for each round.
    
    Returns:
        str: The name of the winner ('Maria' or 'Ben'), or None if no winner.
    """
    if not isinstance(num_rounds, int) or not isinstance(rounds, list):
        return None
    if num_rounds <= 0 or any(not isinstance(n, int) for n in rounds):
        return None
    
    maria_score = 0
    ben_score = 0
    
    for upper_limit in rounds:
        primes = generate_primes(upper_limit)
        if len(primes) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
    
    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
    return None
