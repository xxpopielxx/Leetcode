class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-float("inf")] * n
        if n == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            #case1: okradam i-ty dom
            dp[i] = max(dp[i],dp[i-2] + nums[i])
            #case2: nie okradam go
            dp[i] = max(dp[i], dp[i-1])
        
        return dp[n-1]