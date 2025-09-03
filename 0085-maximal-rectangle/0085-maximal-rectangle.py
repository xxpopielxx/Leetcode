class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0            

        def largest_rectangle_area(heights): #funkcja znajdująxa max rextangle w histogramie
        # taka jak to sobne zadanie na leetcodzie
            stack = []
            heights.append(0)
            res = 0

            for i,h in enumerate(heights):
                while stack and h < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    res = max(res, height*width)
                stack.append(i)
            heights.pop()

            return res
        
        n, m = len(matrix), len(matrix[0])

        heights = [0] * m 
        res = 0
        for i in range(n): #przechodze po kolei po wierszach, aktualizuje histogram
        # wysokości żeby była wkatualna wysokość w kolumnie a następnie wywołuje tą funkcje do
        # histogramu po każdym wierszu i aktualizuje maxa
            for j in range(m):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            res = max(res, largest_rectangle_area(heights))

        return res

            