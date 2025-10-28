class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 !=0:
            return False

        target = sum(nums) // 2

        dp = [False] * (target + 1)

        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
            
            if dp[target]:
                return True
        
        return dp[target]




