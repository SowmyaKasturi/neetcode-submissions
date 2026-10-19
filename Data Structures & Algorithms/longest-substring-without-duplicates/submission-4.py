class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = len(s)
        if right == 1:
            return 1
        j = left
        _t = ""
        count = 0
        for i in range(right):
            j = i + 1
            print(j)
            _t = s[i]
            while j < right:
                if s[j] not in _t:
                    _t += s[j]
                    j += 1
                    print(_t)
                else:
                    break
            count = max(count,len(_t))
        return count