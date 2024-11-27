#!/usr/bin/python3
"""
Module to solve the coin change problem using dynamic programming.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given amount total.

    Args:
        coins (list): The list of coin denominations.
        total (int): The target amount to make.

    Returns:
        int: Fewest number of coins needed to meet the total.
             -1 if the total cannot be met using the given coins.
    """
    if total <= 0:
        return 0

    # Initialize an array for storing the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make total 0

    # Loop through each coin and update the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be formed
    return dp[total] if dp[total] != float('inf') else -1
