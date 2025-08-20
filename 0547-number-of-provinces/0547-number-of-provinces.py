class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False for _ in range(n)]
        cnt = 0

        def matrix_to_adj_list(M):
            n = len(M)
            G = [[] for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    if M[i][j] != 0 and i < j:
                        G[i].append(j)
                        G[j].append(i)

            return G
        
        def visit(u):
            if visited[u]:
                return
            
            visited[u] = True

            for v in G[u]:
                visit(v)
        
        G = matrix_to_adj_list(isConnected)

        for v in range(n):
            if not visited[v]:
                cnt += 1
                visit(v)
        
        return cnt
        

