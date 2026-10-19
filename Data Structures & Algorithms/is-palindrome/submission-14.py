import re
class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        from string import ascii_lowercase
        ascii_s = set(ascii_lowercase) | set("0123456789")
        print(ascii_s)
        a = ord('a')
        z = ord('z')
        if len(s) < 2:
            return True
        
        s= s.lower().replace(" ","")
        s = "".join(map(lambda x: x if x in ascii_s else "",s))
        print(s)
        i = 0
        j = len(s) -1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True