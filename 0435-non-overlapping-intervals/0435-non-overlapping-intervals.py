class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        cnt = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                cnt += 1
            else:
                end = intervals[i][1]
        
        return cnt



            
        