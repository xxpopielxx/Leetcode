class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        tab_atlantic = [[0] * n for _ in range(m)]
        tab_pacific = [[0] * n for _ in range(m)]

        def dfs(i, j, ocean, prev_height):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if ocean[i][j] == 1 or heights[i][j] < prev_height:
                return

            ocean[i][j] = 1

            dfs(i, j + 1, ocean, heights[i][j])
            dfs(i, j - 1, ocean, heights[i][j])
            dfs(i + 1, j, ocean, heights[i][j])
            dfs(i - 1, j, ocean, heights[i][j])
        
        #pacific
        for j in range(n):
            dfs(0, j, tab_pacific, heights[0][j])
        for i in range(m):
            dfs(i, 0, tab_pacific,heights[i][0])

        #atlantic
        for j in range(n):
            dfs(m-1, j, tab_atlantic, heights[m-1][j])
        for i in range(m):
            dfs(i, n-1, tab_atlantic, heights[i][n-1])
        

        #check
        res = []
        for i in range(m):
            for j in range(n):
                if tab_atlantic[i][j] == 1  and tab_pacific[i][j] == 1:
                    res.append([i, j])

        return res