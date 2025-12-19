from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known = {0, firstPerson}
        
        meetings.sort(key=lambda x: x[2])
        
        grouped_meetings = []
        i = 0
        while i < len(meetings):
            current_time = meetings[i][2]
            current_group = []
            while i < len(meetings) and meetings[i][2] == current_time:
                current_group.append(meetings[i])
                i += 1
            
            
            graph = defaultdict(list)
            involved_people = set()
            
            for p1, p2, time in current_group:
                graph[p1].append(p2)
                graph[p2].append(p1)
                involved_people.add(p1)
                involved_people.add(p2)
            
            queue = deque()
            for person in involved_people:
                if person in known:
                    queue.append(person)
            
            #bfs
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in known:
                        known.add(neighbor)
                        queue.append(neighbor)
                        
        return list(known)
