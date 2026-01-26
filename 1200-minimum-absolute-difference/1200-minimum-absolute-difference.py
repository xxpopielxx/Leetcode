class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if len(arr) == 0:
            return []
        arr.sort()
        n = len(arr)
        mini = float("inf")
        for i in range(1, n):
            diff = arr[i] - arr[i-1]
            mini = min(mini, diff)
        
        res = []
        for i in range(1,n):
            if arr[i] - arr[i-1] == mini:
                res.append([arr[i-1], arr[i]])
        return res

