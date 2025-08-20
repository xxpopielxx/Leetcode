class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def edges_to_list(E):
            G = [[] for _ in range(n)]

            for u,v in E:
                G[u].append((v,1))
                G[v].append((u,0))

            return G
        
        G = edges_to_list(connections)
        visited = [False for _ in range(n)]

        def dfs(u):
            visited[u] = True
            cnt = 0

            for v,w in G[u]:
                if not visited[v]:
                    cnt += w
                    cnt += dfs(v)
            
            return cnt
        
        return dfs(0)


        
        