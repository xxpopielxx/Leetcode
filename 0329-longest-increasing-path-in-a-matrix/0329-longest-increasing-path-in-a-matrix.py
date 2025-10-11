class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)] #dp[i][j] - maksymalna ścieżka zaczynajaca się w matrix[i][j]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j):
            if dp[i][j] != 0: #jeśli już zmodyfikowałem to zwracam, przez to złożoność to m*n a nie m*n*dfs bo dzięki memoizacji
            # każdą komórkę przetwarzam raz
                return dp[i][j]

            max_length = 1 #zaczynam od 1 czyli jak tylko matrix[i][j]

            for dx, dy in directions:
                new_x, new_y = i + dx, j + dy
                if 0 <= new_x < n and 0 <= new_y < m and matrix[i][j] < matrix[new_x][new_y]: #jesli w ramach i większy
                    max_length = max(max_length, 1 + dfs(new_x, new_y)) #akrualizuje max_length i wchodzę dalej do rekurencji
            
            dp[i][j] = max_length #akrualizuje dp[i][j]
            return dp[i][j]

        res = 0
        for i in range(n):
            for j in range(m):
               res = max(res, dfs(i,j)) #dla każdego sprawdzam max ścieżke i aktualizuje od razu

        return res 
