from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0 for _ in range(n)]
        Q = deque()

        for i in range(n):
            if colors[i] == 0:
                Q.append(i)
                colors[i] = 1
            
            while len(Q) > 0:
                u = Q.popleft()
                for v in graph[u]:
                    if colors[v] == 0:
                        colors[v] = -1*colors[u]
                        Q.append(v)
                    elif colors[v] == colors[u]:
                        return False
        return True