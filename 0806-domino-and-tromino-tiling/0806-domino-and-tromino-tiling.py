class Solution:
    def numTilings(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 2:
            return 5

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        for i in range(4, n+1):
            dp[i] = 2  * dp[i-1]  + dp[i-3]
        
        return dp[n] % (10**9 + 7)  

        