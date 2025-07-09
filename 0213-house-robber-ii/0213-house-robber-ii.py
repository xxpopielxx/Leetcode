class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-float("inf")] * n
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n-1):
            #case1: okradam i-ty dom
            dp[i] = max(dp[i], dp[i-2] + nums[i])
            #case2: nie okradam go
            dp[i] = max(dp[i], dp[i-1])
        
        dp1 = [-float("inf")] * n
        dp1[0] = 0
        dp1[1] = nums[1]
        dp1[2] = max(nums[1],nums[2])

        for i in range(3,n):
            #case1: okradam i-ty dom
            dp1[i] = max(dp1[i], dp1[i-2] + nums[i])
            #case2: nie okradam go
            dp1[i] = max(dp1[i], dp1[i-1])

        return max(dp[n-2], dp1[n-1])