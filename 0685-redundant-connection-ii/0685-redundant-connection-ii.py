class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        candidate1 = None
        candidate2 = None
        actual_parent = {}

        for u, v in edges:
            if v in actual_parent:
                candidate1 = [actual_parent[v], v]
                candidate2 = [u, v]

                continue
            actual_parent[v] = u

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        for u, v in edges:
            if candidate2 and [u, v] == candidate2:
                continue
            root_u = find(u)       
            root_v = find(v)
            if root_u == root_v:
                if candidate1:
                    return candidate1
                else:
                    return [u, v]
            parent[root_u] = root_v

        return candidate2
            