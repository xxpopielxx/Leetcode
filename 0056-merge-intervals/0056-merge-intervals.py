class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
    
        intervals.sort(key=lambda x: x[0])
        
        res = []
        current = intervals[0]
        
        for i in range(1, len(intervals)):
            next_interval = intervals[i]
            
            if next_interval[0] <= current[1]:
                current[1] = max(current[1], next_interval[1])
            else:
                res.append(current)
                current = next_interval
        
        res.append(current)
        
        return res