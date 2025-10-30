class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        bool_target = [False, False, False]
        tx, ty, tz = target

        for a, b, c in triplets:
            if a > tx or b > ty or c > tz: #pomijam większe bo już nie będe w stanie wrócić do mniejszego targetu
                continue
            
            if a == tx:
                bool_target[0] = True
            if b == ty:
                bool_target[1] = True  
            if c == tz:
                bool_target[2] = True 

            if bool_target[0] and bool_target[1] and bool_target[2]:
                return True

        return all(bool_target)