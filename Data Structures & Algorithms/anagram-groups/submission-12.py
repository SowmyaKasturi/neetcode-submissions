class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for word in strs:
            chars = [0] * 26
            for char in word:
                chars[ord(char) - ord('a')] += 1
            anagram_key = tuple(chars)
            print(anagrams, word)
            anagrams.setdefault(anagram_key,[]).append(word)
        return anagrams.values()
