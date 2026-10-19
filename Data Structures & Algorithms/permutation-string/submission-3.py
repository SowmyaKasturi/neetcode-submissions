import itertools
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26
        char = [0] * 26
        left = 0
        window_size = len(s1)
        for i in s1:
            char[ord(i)-ord('a')] += 1
        for i in range(len(s2)):
            freq[ord(s2[i])-ord('a')] += 1
            if window_size == i-left+1 and freq == char:
                return True
            while i-left+1 >= window_size:
                freq[ord(s2[left])-ord('a')] -= 1
                left += 1
        return False


