class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        visited = [0] * numCourses
        result = []

        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True

            visited[course] = 1
            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False
            visited[course] = 2
            result.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
                
        return result[::-1]
