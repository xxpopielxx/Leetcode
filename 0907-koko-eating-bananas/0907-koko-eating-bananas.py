import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(piles, k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total
        

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            total_h = hours(piles, mid)

            if total_h <= h:
                right = mid
            else:
                left = mid + 1
        
        return left
        