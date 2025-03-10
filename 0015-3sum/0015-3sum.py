class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        result = []
        
        for a in range(len(nums) - 2):
            if a > 0 and nums[a] == nums[a - 1]:  
                continue 
            b, c = a + 1, len(nums) - 1            
            while b < c:
                suma = nums[a] + nums[b] + nums[c]  
                if suma == 0:
                    result.append([nums[a], nums[b], nums[c]])  
                    while b < c and nums[b] == nums[b + 1]:
                        b += 1
                    while b < c and nums[c] == nums[c - 1]:
                        c -= 1    
                    b += 1
                    c -= 1
                elif suma < 0:
                    b += 1
                else:
                    c -= 1
            
        return result
            
        