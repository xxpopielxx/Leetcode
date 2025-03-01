class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board[0])

        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    for g in range(j+1, n):
                        if board[i][j] == board[i][g]:
                            return False
        
        for i in range(n):
            for j in range(n):
                if board[j][i] != ".":
                    for g in range(j+1, n):
                        if board[j][i] == board[g][i]:
                            return False
        
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                seen = set()
                for x in range(3):
                    for y in range(3):
                        num = board[i + x][j + y]
                        if num != ".":
                            if num in seen:
                                return False
                            seen.add(num)
        
        return True

        
        return True



        