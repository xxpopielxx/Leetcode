class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:

            while k > 0 and stack and stack[-1] > digit: #jeśli mogę jeszcze usunąc a mam mniejszą liczbę to usuwam
                stack.pop()
                k -= 1
            stack.append(digit)

        stack = stack[:-k] if k > 0 else stack #jeśli mam jeszcze jakieś usunięcia to usuwam k ostatnich czyli k największych
        #byłoby tak np dla k = 2 i 12345 bo ani razu byśmy nie usunęli w pętli, bo nie było sensu

        res = "".join(stack).lstrip("0") #joinuje do stringa i usuwam ewentualne 0 z lewej strony

        return res if res else "0"
        
