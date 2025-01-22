class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = [False] * (n)
        diagUp = [False] * (2*n)
        diagDown = [False] * (2*n)

        def solve(row):

            if row == n:
                solution = []
                for r in cnt:
                    rowx = ""
                    for thing in r:
                        rowx += thing
                    solution.append(rowx)
                return [solution]

            ans = []
            for col in range(n):
                if not diagUp[row + col] and not diagDown[row - col] and not columns[col]:
                    diagUp[row + col] = True
                    diagDown[row - col] = True
                    columns[col] = True
                    cnt[row][col] = "Q"

                    new_solution = solve(row + 1)
                    if new_solution:
                        ans += new_solution

                    diagUp[row + col] = False
                    diagDown[row - col] = False
                    columns[col] = False
                    cnt[row][col] = "."
            return ans


        cnt = [["." for _ in range(n)] for _ in range(n)]    
        return solve(0)


            
        