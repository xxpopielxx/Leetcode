class Solution:
    def totalNQueens(self, n: int) -> int:
        columns = [False] * (n)
        diagUp = [False] * (2*n)
        diagDown = [False] * (2*n)
        def solve(row):
            cnt = 0
            if row == n:
                return 1

            for col in range(n):
                if not diagUp[row + col] and not diagDown[row - col] and not columns[col]:
                    diagUp[row + col] = True
                    diagDown[row - col] = True
                    columns[col] = True
                    cnt += solve(row + 1)
                    diagUp[row + col] = False
                    diagDown[row - col] = False
                    columns[col] = False
            return cnt
        return solve(0)



        