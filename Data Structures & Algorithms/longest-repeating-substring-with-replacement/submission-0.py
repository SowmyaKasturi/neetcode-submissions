class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0
        freq = [0] * 26  # Frequency of characters (assuming uppercase A-Z)
        result = 0

        for right in range(len(s)):
            freq[ord(s[right]) - ord('A')] += 1
            max_count = max(max_count, freq[ord(s[right]) - ord('A')])

            # If replacements needed > k, shrink window
            while (right - left + 1) - max_count > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result