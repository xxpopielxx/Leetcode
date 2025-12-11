class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_bounds = {}
        y_bounds = {}
        
        for x,y in buildings:
            if x not in x_bounds:
                x_bounds[x] = [float("inf"), float("-inf")]
            x_bounds[x][0] = min(x_bounds[x][0], y)
            x_bounds[x][1] = max(x_bounds[x][1], y)

            if y not in y_bounds:
                y_bounds[y] = [float("inf"), float("-inf")]
            y_bounds[y][0] = min(y_bounds[y][0], x)
            y_bounds[y][1] = max(y_bounds[y][1], x)
        
        cnt = 0

        for x,y in buildings:
            is_covered_x = x_bounds[x][0] < y < x_bounds[x][1]
            is_covered_y = y_bounds[y][0] < x < y_bounds[y][1]

            if is_covered_x and is_covered_y:
                cnt += 1
        
        return cnt
