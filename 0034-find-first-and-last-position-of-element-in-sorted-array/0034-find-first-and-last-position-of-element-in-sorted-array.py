class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                end = i 

                while (end + 1) <= (n-1) and nums[end + 1] == target:
                    end += 1
                return [i, end]

        return [-1,-1]
        