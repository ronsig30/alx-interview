#!/usr/bin/python3
def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of integers representing the values of coins.
        total (int): The total amount to be made.

    Returns:
        int: Fewest number of coins needed to meet total,
             0 if total is 0 or less,
             -1 if total cannot be met by any number of coins.
    """
    # Return 0 if the total is 0 or less
    if total <= 0:
        return 0

    # Initialize the dp array with infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            # Update the dp array if we find a smaller number of coins
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means we cannot make that amount
    return dp[total] if dp[total] != float('inf') else -1
