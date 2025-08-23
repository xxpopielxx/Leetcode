import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        Q = []
        current = startFuel
        cnt = 0
        i = 0
        n = len(stations)

        while current < target:
            while i < n and stations[i][0] <= current:
                heapq.heappush(Q, -stations[i][1])
                i += 1

            if not Q:
                return -1

            maxi = -heapq.heappop(Q)
            current += maxi
            cnt += 1
        
        return cnt

            
