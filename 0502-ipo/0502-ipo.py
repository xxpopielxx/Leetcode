import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = []
        for i in range(len(profits)):
                pairs.append((capital[i], profits[i]))
        pairs.sort()

        heap = []
        current_capital = w
        index = 0
        n = len(pairs)

        for _ in range(k):
            while index < n and current_capital >= pairs[index][0]:
                heapq.heappush(heap, -pairs[index][1])
                index += 1
            
            if not heap:
                break
            
            current_capital += -heapq.heappop(heap)
        
        return current_capital
                
                    


