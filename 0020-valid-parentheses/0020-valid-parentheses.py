class Solution:
    def isValid(self, s: str) -> bool:
        para = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack or para.get(ch) != stack.pop():
                    return False

        return not stack

        