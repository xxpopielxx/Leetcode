import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        pairs = []
        potions.sort()

        for spell in spells:
            left = 0
            right = m-1
            current = m
            min_potion = math.ceil(success/spell)

            while left <= right:
                mid = left + (right - left) // 2

                if potions[mid] < min_potion:
                    left = mid + 1
                else:
                    right = mid - 1
            
            pairs.append(m - left)
        
        return pairs
                




        