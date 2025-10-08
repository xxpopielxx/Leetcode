class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        #prefix: wszystkie na lewo
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        #suffix: wszystkie na prawo
        suffix = 1
        for j in range(n-1,-1,-1):
            res[j] *= suffix
            suffix *= nums[j]
    
        return res