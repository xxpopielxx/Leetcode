class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        right_counts = {}
        for x in nums:
            right_counts[x] = right_counts.get(x, 0) + 1
            
        left_counts = {}
        cnt = 0
        
        for x in nums:
            right_counts[x] -= 1
            
            wall = x * 2
            
            if wall in right_counts:
                l = left_counts.get(wall, 0)
                r = right_counts.get(wall, 0)
                
                cnt += (l * r)
            
            left_counts[x] = left_counts.get(x, 0) + 1
            
        return cnt % MOD