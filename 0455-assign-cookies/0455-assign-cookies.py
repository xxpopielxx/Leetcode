class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child_i = cookie_j = 0
        content = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                content += 1
                child_i += 1
                cookie_j += 1
            else:
                cookie_j += 1
        return content

