from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        n = len(points)

        for i in range(n):
            distance = sqrt(points[i][0]**2 + points[i][1]**2)
            dist.append((distance, i))
        
        def heapify(T,n,i):
            max_ind = i
            l = 2*i + 1
            r = 2*i + 2
            if l < n and T[l][0] > T[max_ind][0]:
                max_ind = l
            if r < n and T[r][0] > T[max_ind][0]:
                max_ind = r
            if max_ind != i:
                T[i], T[max_ind] = T[max_ind], T[i]
                heapify(T,n,max_ind)


        def max_heap(T):
            n = len(T)
            for i in range((n-1)//2, -1, -1):
                heapify(T,n,i)
        
        max_heap(dist)
        for i in range(n - 1, 0, -1):
            dist[0], dist[i] = dist[i],dist[0]
            heapify(dist, i, 0)

        res = []
        for i in range(k):
            res.append(points[dist[i][1]])
        return res