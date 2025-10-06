import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        connected = 0
        mini = 0

        heap = [(0,0)] # koszt, wierzchołek

        while connected < n:
            cost, vertex = heapq.heappop(heap)
            if visited[vertex]:
                continue
            visited[vertex] = True
            mini += cost
            connected += 1

            for i in range(n):
                if not visited[i]:
                    dist = abs(points[vertex][0] - points[i][0]) + abs(points[vertex][1] - points[i][1])
                    heapq.heappush(heap, (dist, i))
        
        return mini
