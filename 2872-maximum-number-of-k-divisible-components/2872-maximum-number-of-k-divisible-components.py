class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        adj_list = [[] for _ in range(n)]
        for v, u in edges:
            adj_list[v].append(u)
            adj_list[u].append(v)

        def dfs(current_node, parent_node):
            sum_ = 0

            for u in adj_list[current_node]:
                if u != parent_node:
                    sum_ += dfs(u, current_node)
            
            sum_ += values[current_node]
            
            if sum_ % k == 0:
                cnt[0] += 1
                return 0 
            
            return sum_
            
        cnt = [0]
        dfs(0, -1)
        return cnt[0]

        