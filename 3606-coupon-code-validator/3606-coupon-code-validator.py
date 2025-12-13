class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        is_valid_char = [False] * 128
    
        allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
        for char in allowed_chars:
            is_valid_char[ord(char)] = True

        valid_categories = {"electronics", "grocery", "pharmacy", "restaurant"}
        
        valid_coupons = []

        n = len(code)
        for i in range(n):
            if not isActive[i]:
                continue
            if businessLine[i] not in valid_categories:
                continue
            
            c = code[i]
            if not c:
                continue
            
            is_code_ok = True
            for char in c:
                if ord(char) > 127 or not is_valid_char[ord(char)]:
                    is_code_ok = False
                    break
            
            if is_code_ok:
                valid_coupons.append((businessLine[i], c))
        valid_coupons.sort()

        return [item[1] for item in valid_coupons]