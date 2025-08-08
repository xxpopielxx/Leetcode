class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        dp = [[] for _ in range(n)]
        dp[0] = [0]
        
        for i in range(n):
            for last_jump in dp[i]:
                for jump in (last_jump - 1, last_jump, last_jump + 1):
                    if jump > 0:
                        next_pos = stones[i] + jump

                        for j in range(i+1, n):
                            if stones[j] == next_pos:
                                if jump not in dp[j]:
                                    dp[j].append(jump)
                                break
                            elif stones[j] > next_pos:
                                break
        
        if len(dp[n-1]) > 0:
            return True
        return False



        