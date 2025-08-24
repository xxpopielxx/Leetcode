class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1]) #sortuje po końcach
        n = len(points)
        cnt = 1
        end = points[0][1] #trzymam najmniejszy koniec przecinających się przedziałów

        for i in range(1, n):
            left, right = points[i]
            if left <= end: #jeśli się przecinają no to nic nie robie
                continue
            else:   #jesli rozłączne to dodaje strzałe oraz aktualizuje koniec na aktualny koniec przediału      
                cnt += 1
                end = points[i][1]

        return cnt



        


        