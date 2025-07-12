class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        while left < n-1 and nums[left] <= nums[left+1]: #znajduje lewą granice
            left += 1
        if left == n-1:
            return 0

        right = n-1
        while right > 0 and nums[right] >= nums[right-1]: #znajduje prawą granicę
            right -= 1

        min_val = min(nums[left:right+1]) #max dla tego przedziału
        max_val = max(nums[left:right+1]) #min dla tego przedziału

        #dołączam wszystkie elementy na lewo większe od min
        while left > 0 and nums[left-1] > min_val: 
            left -= 1

        #dołączam wszystkie elementy na prawo mniejesze od max
        while right < n-1 and nums[right + 1] < max_val:  
            right += 1

        return right - left + 1 
                        

        