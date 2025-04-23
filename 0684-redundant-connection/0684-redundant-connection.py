class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        number_of_nodes = len(edges)
        parents = [i for i in range(number_of_nodes + 1)]

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            parents[find(u)] = find(v)

        