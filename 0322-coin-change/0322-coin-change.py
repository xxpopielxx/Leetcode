class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp[i] = min coins to make amount i
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1


        