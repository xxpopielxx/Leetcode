class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = max longest subsequence to i-th index in text1 and j-th index in text2
        n, m = len(text1), len(text2)
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0

        for i in range(1, n): #wypełaniam base case
            dp[i][0] = 1 if dp[i-1][0] == 1 or text1[i] == text2[0] else 0
        
        for j in range(1, m):
            dp[0][j] = 1 if dp[0][j-1] == 1 or text1[0] == text2[j] else 0
        
        for i in range(1, n):
            for j in range(1, m):
                if text1[i] == text2[j]: #jeśli się równają
                    dp[i][j] = dp[i-1][j-1] + 1
                else:   #jeśli się nie równają no to max z pominiecia jedengo znaku
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[n-1][m-1]
                


        