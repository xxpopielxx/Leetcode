class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        current = 0
        for i in range(k):
            current += nums[i]

        res = current/k

        i = 0
        j = k-1

        while j < n-1:

            current = current + nums[j+1] - nums[i]
            if current/k > res:
                res = current/k

            j += 1
            i += 1
        
        return res

        
         