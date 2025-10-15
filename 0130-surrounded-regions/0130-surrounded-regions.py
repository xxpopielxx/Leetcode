class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n,m = len(board), len(board[0])

        def dfs(i,j):
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != "O":
                return
            board[i][j] = "#"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(n): #zaznaczam wszystkie O które tworzą region i mają O na krawędzi
            dfs(i,0)
            dfs(i,m-1)
        for j in range(m):
            dfs(0, j)
            dfs(n-1, j)

        for i in range(n): #zamieniam to co # na O a to co O na X
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        



        