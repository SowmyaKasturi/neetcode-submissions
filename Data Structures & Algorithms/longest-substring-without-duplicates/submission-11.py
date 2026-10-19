class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i , j = 0, 0
        max_len = 0
        while i < len(s):
            seen = set()
            seen.add(s[i])
            j = i + 1
            while j < len(s):
                if s[j] not in seen:
                    seen.add(s[j])
                else:
                    break
                j += 1
            max_len = max(max_len, len(seen))
            i += 1
        return max_len