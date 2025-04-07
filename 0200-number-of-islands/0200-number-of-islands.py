class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        cnt = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    cnt += 1
                    self.dfs(grid, i, j, rows, cols)
        return cnt
        
    def dfs(self, grid, i, j, rows, cols):
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != "1":
            return
        grid[i][j] = '0' 
        self.dfs(grid, i+1, j, rows, cols)
        self.dfs(grid, i-1, j, rows, cols)
        self.dfs(grid, i, j+1, rows, cols)
        self.dfs(grid, i, j-1, rows, cols)
        