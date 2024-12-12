#!/usr/bin/python3
"""
Prime Game
"""


def sieve_of_eratosthenes(n):
    """
    Generate prime numbers up to n using the Sieve of Eratosthenes algorithm.

    Args:
      n: The upper limit to generate primes to.

    Returns:
      A list of prime numbers up to n.
    """
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
    return primes


def can_win(n):
    """
    Determines if the first player can win the game with n integers.

    Args:
      n: The upper limit of the integers (1 to n).

    Returns:
      True if the first player can win, False otherwise.
    """
    if n < 2:
        return False
    primes = sieve_of_eratosthenes(n)
    if len(primes) % 2 == 0:
        return False
    else:
        return True


def isWinner(x, nums):
    """
    Determines the winner of the game based on rounds and numbers.

    Args:
        x (int): The number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str: The name of the player that won the most rounds.
        If the winner cannot be determined, return None.
    """

    if x == 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
