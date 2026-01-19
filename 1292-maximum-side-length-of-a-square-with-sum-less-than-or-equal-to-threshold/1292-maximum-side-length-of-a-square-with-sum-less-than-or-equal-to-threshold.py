class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # P[i][j] = current_val + top + left - top_left_overlap
                P[i][j] = mat[i-1][j-1] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]
        
        max_side = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                current_side = max_side + 1
                
                if i >= current_side and j >= current_side:
                    r1, c1 = i - current_side, j - current_side
                    
                    total = P[i][j] - P[r1][j] - P[i][c1] + P[r1][c1]
                    
                    if total <= threshold:
                        max_side += 1
                        
        return max_side
        