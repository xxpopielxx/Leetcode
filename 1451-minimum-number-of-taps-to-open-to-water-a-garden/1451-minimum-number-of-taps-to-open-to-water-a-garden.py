
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        pairs = []
        for i in range(len(ranges)):
            if ranges[i] == 0:
                continue
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            pairs.append((left, right))
        pairs.sort()
        
        if not pairs or pairs[0][0] > 0:
            return -1
        
        cnt = 0
        current_end = 0
        i = 0
        max_reach = 0

        while current_end < n:
            found = False
            while i < len(pairs) and pairs[i][0] <= current_end:
                max_reach = max(max_reach, pairs[i][1])
                i += 1
                found = True
            
            if not found:
                return -1
            
            cnt += 1
            current_end = max_reach
        
        return cnt
        
        