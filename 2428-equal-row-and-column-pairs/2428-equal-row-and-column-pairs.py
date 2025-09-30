class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_map = {}

        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in row_map:
                row_map[row_tuple] += 1
            else:
                row_map[row_tuple] = 1
        
        res = 0
        for col in range(n):
            col_tuple = tuple(grid[row][col] for row in range(n))
            if col_tuple in row_map:
                res += row_map[col_tuple]

        
        return res