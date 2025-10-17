class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def edges_to_list(E, n):
            G = [[] for _ in range(n)]

            for u,v,w in E:
                G[u].append((v,w))

            return G
        
        import heapq

        def dijkstra(G, start, k):
            n = len(G)

            visited = [[False] * (k+2) for _ in range(n)]
            distances = [[float('inf')] * (k+2) for _ in range(n)]

            Q = []
            heapq.heappush(Q, (0, start, 0))

            distances[start][0] = 0

            while Q:
                cost, u, stop = heapq.heappop(Q)

                if visited[u][stop]:
                    continue
                visited[u][stop] = True

                for v, w in G[u]:
                    new_cost = cost + w
                    new_stop = stop + 1

                    if new_stop <= k + 1 and new_cost < distances[v][new_stop]:
                        distances[v][new_stop] = new_cost
                        heapq.heappush(Q, (new_cost, v, new_stop))

            return distances
        
        G = edges_to_list(flights, n)
        distances = dijkstra(G, src, k)

        res = min(distances[dst])
        return res if res != float('inf') else -1
