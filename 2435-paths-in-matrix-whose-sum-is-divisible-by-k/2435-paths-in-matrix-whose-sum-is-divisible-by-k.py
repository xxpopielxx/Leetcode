class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7   
        #dp[i][j][r] przechowuje liczbę ścieżek do pola (i,j) dających resztę r
        dp = [[[0] * k for _ in range(n)] for _ in range(m)] 

        start_val = grid[0][0]
        dp[0][0][start_val % k] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                val = grid[i][j]

                for r in range(k):
                    #jaką resztę musieliśmy mieć wcześniej, żeby teraz uzyskać r
                    prev_r = (r - val) % k

                    #jeśli przyszlismu z góry
                    if i > 0:
                        dp[i][j][r] = (dp[i][j][r] + dp[i-1][j][prev_r]) % MOD
                    
                    #jeśli przyszliśmy z lewej
                    if j > 0:
                        dp[i][j][r] = (dp[i][j][r] + dp[i][j-1][prev_r]) % MOD
        return dp[m-1][n-1][0]