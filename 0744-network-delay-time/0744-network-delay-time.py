import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #dijkstra -> check res
        G = [[] for _ in range(n+1)]
        for u,v,w in times:
            G[u].append((v, w))
        
        distances = [float("inf")] * (n+1)
        distances[k] = 0

        heap = [(0, k)] #distance, vertex

        while heap:
            dist, v = heapq.heappop(heap)
            
            if dist > distances[v]:
                continue

            for u,w in G[v]:
                new_dist = dist + w
                if new_dist < distances[u]:
                    distances[u] = new_dist
                    heapq.heappush(heap, (new_dist, u))

        res = max(distances[1:]) #ignore index 0
        return -1 if res == float("inf") else res