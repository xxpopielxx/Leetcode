class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        dp = [[] for _ in range(n)]
        dp[0] = [0]
        
        for i in range(n):
            for last_jump in dp[i]:
                for j in range(i+1, n):
                    jump = stones[j] - stones[i]
                    if jump < last_jump - 1:
                        continue
                    if jump > last_jump + 1:
                        break # dalsze kamienie są jeszcze dalej, więc można przerwać
                    if jump not in dp[j]:
                        dp[j].append(jump)

        return len(dp[-1]) > 0
        



        