import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        n = len(courses)
        courses.sort(key = lambda x: x[1])
        
        heap = []
        total_days = 0

        for duration, lastday in courses:
            total_days += duration
            heapq.heappush(heap, -duration)

            if total_days > lastday:
                longest = -heapq.heappop(heap)
                total_days -= longest
        
        return len(heap)

        
