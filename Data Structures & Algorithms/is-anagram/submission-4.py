class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # from collections import Counter
        # return Counter(s) == Counter(t)
        # to avoid counter overhead we can user zip and array
        if len(s) != len(t):
            return False
        if s == t:
            return True
        count = [0] * 26
        for chr_s, chr_t in zip(s,t):
            count[ord(chr_s) - ord('a')] += 1
            count[ord(chr_t) - ord('a')] -= 1
        return all( _ == 0 for _ in count)
