class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        if len(strs) == 1:
            return 0
        prev = [s for s in strs[0]]
        deleted = [False] * n
        res = 0

        for x in range(1, len(strs)):
            for i in range(n):
                if strs[x][i] < prev[i] and not deleted[i]:
                    res += 1
                    deleted[i] = True
                prev[i] = strs[x][i]
        return res


        