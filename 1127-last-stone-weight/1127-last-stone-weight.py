import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        Q = []
        for stone in stones:
            heapq.heappush(Q, -stone)
        
        while len(Q) > 1:
            first = -heapq.heappop(Q)
            second = -heapq.heappop(Q)

            if first != second:
                heapq.heappush(Q, -(first - second))
        
        return -Q[0] if Q else 0