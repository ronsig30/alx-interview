#!/usr/bin/python3
"""
This module contains the makeChange function
to find the fewest number of coins to meet a total amount.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of coin denominations.
        total (int): The total amount.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Return 0 if total is 0 or less.
             Return -1 if total cannot be met with the available coins.
    """
    memo = {}

    def helper(rem):
        """
        Helper function to recursively find the fewest coins for the remainder.

        Args:
            rem (int): Remaining amount to find coins for.

        Returns:
            int: Fewest number of coins needed to meet the remainder.
                 Return -1 if it's not possible.
        """
        if rem < 0:
            return -1
        if rem == 0:
            return 0

        # Check if the result is already in the memo
        if rem in memo:
            return memo[rem]

        # Initialize the minimum number of coins as infinity
        min_coins = float('inf')

        # Try using each coin and solve the subproblem recursively
        for coin in coins:
            res = helper(rem - coin)
            if res >= 0:  # If it's possible to make rem - coin
                min_coins = min(min_coins, res + 1)

        # Store the result in the memo, or -1 if no solution was found
        memo[rem] = -1 if min_coins == float('inf') else min_coins
        return memo[rem]

    # Call the helper function and return the result for the total amount
    return helper(total)
