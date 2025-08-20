class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False for _ in range(n)]
        
        def visit(u):
            if visited[u]:
                return 
                
            visited[u] = True

            for v in rooms[u]:
                visit(v)
        
        visit(0)

        for val in visited:
            if val == False:
                return False
        
        return True