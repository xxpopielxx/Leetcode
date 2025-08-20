from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minutes = 0
        Q = deque([])
        fresh_cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    Q.append((i,j,0))
                elif grid[i][j] == 1:  
                    fresh_cnt += 1

        if fresh_cnt == 0:
            return 0        
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while Q:
            row, col, time = Q.popleft()
            minutes = max(minutes, time)

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    Q.append((new_row, new_col, time + 1))
                    fresh_cnt -= 1
        
        return minutes if fresh_cnt == 0 else -1