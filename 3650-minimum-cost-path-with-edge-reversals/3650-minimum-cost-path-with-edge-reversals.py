class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))
  
        pq = [(0, 0)]
    
        dist = [float('inf')] * n
        dist[0] = 0
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            
            if u == n - 1:
                return d
            for v, weight in graph[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
                    
        return -1
                