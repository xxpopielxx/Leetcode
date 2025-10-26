import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        Q = []
        Q.append((grid[0][0], 0, 0))
        maxis = grid
        visited = [[False] * n for _ in range(n)]
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while Q:
            current, i, j = heapq.heappop(Q)

            if (i,j) == (n-1, n-1):
                return current
            
            if visited[i][j] and maxis[i][j] <= current:
                continue

            visited[i][j] = True
            maxis[i][j] = current


            for di, dj in moves:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < n and 0 <= nj < n:
                    new_current = max(current, grid[ni][nj])

                    if not visited[ni][nj] or new_current < maxis[ni][nj]:
                        heapq.heappush(Q, (new_current, ni, nj))

        

