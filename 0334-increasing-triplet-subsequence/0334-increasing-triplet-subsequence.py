class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        min_a = float("inf")
        min_b = float("inf")

        for num in nums:
            if num <= min_a:
                min_a = num

            elif num <= min_b:
                min_b = num

            else:
                return True
        
        return False