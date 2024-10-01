#!/usr/bin/python3
"""
Defines isWinner function to determine the game winner.
"""


def sieve_of_eratosthenes(n):
    """Returns a list of prime numbers up to n using the Sieve of Eratosthenes.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Arguments:
    x -- number of rounds
    nums -- list of n values, one per round

    Returns:
    Name of the player with the most wins or None if it cannot be determined.
    """
    if x < 1 or not nums:
        return None

    # Find the largest n in nums to precompute primes once
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Cache to store results of rounds
    results = [0] * (max_n + 1)

    # Determine results for each n
    for n in range(1, max_n + 1):
        primes_up_to_n = [p for p in primes if p <= n]
        turn = 0  # Maria's turn if even, Ben's if odd
        visited = [False] * (n + 1)

        for p in primes_up_to_n:
            if not visited[p]:
                for multiple in range(p, n + 1, p):
                    visited[multiple] = True
                turn += 1

        results[n] = "Maria" if turn % 2 == 1 else "Ben"

    # Count wins for Maria and Ben
    maria_wins = sum(1 for n in nums if results[n] == "Maria")
    ben_wins = sum(1 for n in nums if results[n] == "Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
