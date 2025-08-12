class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        it = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[it], nums[i] = nums[i], nums[it]
                it += 1



        