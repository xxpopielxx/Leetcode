class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_prod = min_prod = result = nums[0]
        
        for num in nums[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod  # Swap cause multiplying by - flips min/max
            
            max_prod = max(num, max_prod * num) #rozpoczynam nowy, poprzedni * num
            min_prod = min(num, min_prod * num) #to samo tylko dla ujemnych
            
            result = max(result, max_prod)
        
        return result
        
