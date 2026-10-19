class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        _hash = {}
        if len(s) != len(t):
            return False
        if s == t:
            return True
        # for i in s:
        #     _hash.setdefault(i,0)
        #     _hash[i] += 1
        # _shash = {}
        # for i in t:
        #     if i not in _hash:
        #         return False
        #     _shash.setdefault(i,0)
        #     _shash[i] += 1
        # for i in _hash:
        #     if _shash[i] != _hash[i]:
        #         return False

        # return True
        freq_s = Counter(s)
        freq_t = Counter(t)
        return freq_s == freq_t
            
