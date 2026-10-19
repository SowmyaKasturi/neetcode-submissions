class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = len(s)
        if right == 1:
            return 1
        j = 0
        _t = set()
        count = 0
        for i in range(right):
            while s[i] in _t:
                _t.remove(s[j])
                j += 1 
            count = max(count,i-j+1)
            _t.add(s[i])
        return count