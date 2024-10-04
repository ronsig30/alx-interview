#!/usr/bin/python3


def makeChange(coins, total):
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Create a list to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Loop through each coin
    for coin in coins:
        # Update the dp array for all amounts from coin to total
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    ''' If dp[total] is still infinity, return -1 indicating it's not possible
    to form total '''
    return dp[total] if dp[total] != float('inf') else -1
