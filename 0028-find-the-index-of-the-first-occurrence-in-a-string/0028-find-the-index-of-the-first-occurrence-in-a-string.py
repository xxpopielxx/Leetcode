class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1 = len(haystack)
        l2 = len(needle)
        for i in range(l1 - (l2 -1)):
            if haystack[i] == needle[0]:
                cnt = 1
                c = i + 1
                length = l2 - 1
                flag = True
                while length != 0:
                    if needle[cnt] != haystack[c]:
                        flag = False
                        break
                    length -= 1
                    cnt += 1
                    c += 1
                if flag:
                    return i
        return -1
                        
                           