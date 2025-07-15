class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0] * n for _ in range(m)]

        # 1 - wartość bo jeśli dodatnie no to potrzebujemy tylko 1 a jeśli ujemne to potrzebujemy 1 - wartośc czyli np (1 -(-5)) = 6
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])

        #initialize last row
        for j in range(n-2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])
        
        #initialize last column
        for i in range(m-2, -1, -1):
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
        
        #fill the rest
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                mini = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, mini - dungeon[i][j])

        return dp[0][0]
