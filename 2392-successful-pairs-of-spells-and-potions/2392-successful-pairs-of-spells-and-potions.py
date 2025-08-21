class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        pairs = []
        potions.sort()

        for spell in spells:
            left = 0
            right = m-1
            current = m

            while left <= right:
                mid = left + (right - left) // 2

                if spell * potions[mid] >= success:
                    current = mid
                    right = mid - 1 
                else:
                    left = mid + 1
            
            pairs.append(m - current)
        
        return pairs
                




        