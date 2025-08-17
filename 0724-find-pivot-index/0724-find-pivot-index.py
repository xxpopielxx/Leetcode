class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            if left == right:
                return i
        
        return -1

        