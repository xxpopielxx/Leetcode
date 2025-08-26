import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pairs = []
        n = len(speed)
        for i in range(n):
            pairs.append((speed[i], efficiency[i]))
        pairs.sort(key = lambda x: x[1], reverse = True)

        maxi = -float("inf")
        heap = []
        total_speed = 0
        for spd, efficiency in pairs:
            heapq.heappush(heap, spd)
            total_speed += spd
            if len(heap) > k:
                total_speed -= heapq.heappop(heap)
            maxi = max(maxi, total_speed * efficiency)
        
        return maxi % (10**9 + 7)
