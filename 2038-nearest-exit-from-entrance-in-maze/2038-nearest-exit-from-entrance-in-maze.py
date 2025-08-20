from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        start_row, start_col = entrance
        maze[start_row][start_col] = "+"

        Q = deque([(start_row, start_col, 0)])

        while Q:
            row, col, steps = Q.popleft()

            if (row == 0 or row == m-1 or col == 0 or col == n-1) and steps > 0:
                return steps

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and maze[new_row][new_col] == ".":
                    maze[new_row][new_col] = "+"
                    Q.append((new_row, new_col, steps + 1))

        return -1


