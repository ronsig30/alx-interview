#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """Generate a list of primes up to max_n using the Sieve"""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    return is_prime


def calculate_prime_counts(max_n, is_prime):
    """Calculate the cumulative count of primes"""
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)
    return prime_count


def isWinner(x, nums):
    """
    Determine the winner of the game based on the rules.

    Parameters:
        x (int): Number of rounds.
        nums (list): Array of n for each round.

    Returns:
        str: Name of the player with the most wins.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)  # Find the maximum number in nums
    is_prime = sieve_of_eratosthenes(max_n)
    prime_count = calculate_prime_counts(max_n, is_prime)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Determine the number of primes up to n
        primes_up_to_n = prime_count[n]

        # Maria wins if the count of primes is odd, otherwise Ben wins
        if primes_up_to_n % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Example Usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
