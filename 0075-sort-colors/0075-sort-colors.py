class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1

            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        """
        Do not return anything, modify nums in-place instead.
        """
        