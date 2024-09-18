Explanation of the Code:

    Initial Check: If the total amount is 0 or less, we immediately return 0, as no coins are needed.

    Dynamic Programming Array: We create a list dp where dp[i] will hold the minimum number of coins needed to make the amount i. We initialize all values to infinity (float('inf')), except for dp[0], which is set to 0.

    Coin Loop: For each coin in the coins list, we iterate through possible amounts from that coin's value up to the target total. For each amount, we check if we can achieve that amount by using the current coin. If using the coin reduces the number of coins needed compared to what we've already recorded, we update dp[amount].

    Final Check: After processing all coins, we check dp[total]. If it remains infinity, it means that the total cannot be formed with the given coins, so we return -1. Otherwise, we return the value in dp[total], which is the minimum number of coins needed

Complexity Analysis:

    Time Complexity: O(n * m), where n is the total amount and m is the number of coin denominations.
    Space Complexity: O(n), as we maintain an array of size n + 1.

This implementation ensures that we find the optimal solution efficiently while adhering to the specified requirements.
