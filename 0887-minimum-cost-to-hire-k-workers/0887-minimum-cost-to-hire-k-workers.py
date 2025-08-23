import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = []
        n = len(wage)
        for i in range(n):
            pairs.append((wage[i] / quality[i], quality[i])) 
        pairs.sort() #sortuje po jakości pracy czyli wage / quality

        heap = []
        current = 0
        res = float("inf")

        for efficiency, quality in pairs: #zaczynam o nnajlepszej wydajności, po to ze za każdym razem
        #dzięki posortowamiu mam największą wydajność w sensie że najgorsza czyli ją muszę użyć
            heapq.heappush(heap, -quality)
            current += quality
            if len(heap) > k: #jesli większy to usuwam największe współczynnik * quality czyli im większe
            #quality tym większa płąca
                current += heapq.heappop(heap)
            if len(heap) == k: #jeśli == k no to aktualizuje
                res = min(res, current * efficiency)

        return res


        
            
            

            
        