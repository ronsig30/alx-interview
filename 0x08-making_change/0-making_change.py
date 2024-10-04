#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with a large number (inf)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make amount 0

    # Iterate over each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means we cannot make that amount
    return dp[total] if dp[total] != float('inf') else -1
