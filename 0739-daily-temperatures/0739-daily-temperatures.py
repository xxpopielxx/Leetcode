class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0] * n

        for i in range(n):
            # While current temperature is warmer than temperature at top of stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            
            stack.append(i)

        return result
        