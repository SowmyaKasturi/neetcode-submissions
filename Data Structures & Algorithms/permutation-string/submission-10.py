import itertools
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26
        char = [0] * 26
        left = 0
        for i in s1:
            char[ord(i)-ord('a')] += 1
        for i in range(len(s2)):
            freq[ord(s2[i])-ord('a')] += 1
            
            if i-left+1 > len(s1):
                freq[ord(s2[left])-ord('a')] -= 1
                left += 1
            
            if freq == char:
                return True
        return False


