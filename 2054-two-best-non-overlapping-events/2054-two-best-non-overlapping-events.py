class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        Q = []

        max_val = 0
        res = 0

        for start, end, value in events:
            while Q and Q[0][0] < start:
                _, v = heapq.heappop(Q)
                max_val = max(max_val, v)
            
            res = max(res, value + max_val)

            heapq.heappush(Q,(end, value))

        return res