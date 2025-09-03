class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix[0]), len(matrix)
        dp = [[0] * m for _ in range(n)]
        #dp[i][j] - maksymalne wymiary kwadratu gdzie dp[i][j] to lewy górny róg kwadratu
        #base case
        maxi = 0
        for i in range(m): #wypełniam skrajną kolumne i wiersz od dołu
            dp[n-1][i] = 1 if matrix[n-1][i] == "1" else 0
            maxi = max(maxi, dp[n-1][i])
        for j in range(n-1):
            dp[j][m-1] = 1 if matrix[j][m-1] == "1" else 0
            maxi = max(maxi, dp[j][m-1])
        
        for i in range(n-2, -1 ,-1): #zaczynam wypełniac od dołu do góry pp wypełnieniu base caseów
            for j in range(m-2, -1, -1):
                if matrix[i][j] == "0": #jeśli 0 no to cały kwadrat 0
                    dp[i][j] = 0
                else: #jeśli nie 0 no to biorę minimum z otaczających i porzeszerzam o tyle kwadrat
                #chodi o to że jak np będzie dookoła 3, 2, 1 no to mogę poszerczyć o 1 tylko a nie o 3
                    add = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                    dp[i][j] = add + 1

                maxi = max(maxi, dp[i][j])
        
        return maxi*maxi
        


