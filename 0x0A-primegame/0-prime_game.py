#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """Return a list of primes up to max_n using the Sieve of Eratosthenes."""
    primes = []
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, max_n + 1):
        if is_prime[number]:
            primes.append(number)
            for multiple in range(number * 2, max_n + 1, number):
                is_prime[multiple] = False

    return primes


def isWinner(x, nums):
    """Determines the winner of the prime game."""
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_set = set(primes)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        current_set = set(range(1, n + 1))
        turn = True

        while True:
            current_primes = sorted([p for p in prime_set if p <= n if p in current_set])
            if not current_primes:
                if turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            chosen_prime = current_primes[0]
            current_set -= set(range(chosen_prime, n + 1, chosen_prime))

            turn = not turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
