class Solution:
    from collections import Counter
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        if s == t:
            return t
        count_t = Counter(t)
        right = 0
        req_l = len(count_t)
        char_count = {}
        left = 0
        formed_char = 0
        min_window = ""
        min_length = float('inf')
        while right < len(s):
            char = s[right]
            char_count[char] = char_count.get(char,0) + 1
            if char in t and char_count[char] == count_t[char]:
                formed_char += 1
                print("here", char,right,formed_char, req_l, char_count, count_t)
                
            while left <= right and formed_char == req_l:
                print("here2", char,right,formed_char, req_l, char_count, count_t)
                if right-left+1 < min_length:
                    min_length = right-left+1
                    min_window = s[left:right+1]
                left_c = s[left]
                char_count[left_c] -= 1
                if left_c in t and char_count[left_c] < count_t[left_c]:
                    formed_char -= 1
                left += 1
            right += 1
        return min_window