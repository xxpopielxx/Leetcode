import collections
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Values are lists of destinations
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets, reverse = True): #sortuje reverse zeby potem mieć najmniejszy leksykograficznie pierwszy
            graph[a].append(b)
        
        res = []

        def dfs(airport):

            while graph[airport]:
                next_airport = graph[airport].pop() #biorę najmniejszy leksykograficznie
                dfs(next_airport) #wchodze w rekurencje
            
            res.append(airport)

        dfs("JFK")

        return res[::-1]