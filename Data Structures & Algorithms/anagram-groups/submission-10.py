class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        anagram_hash = {}
        for i in strs:
            sort_i = [0] *26
            for ch in i:
                sort_i[ord(ch)-ord('a')] += 1
            anagram_hash.setdefault(tuple(sort_i),[]).append(i)
        return list(anagram_hash[i] for i in anagram_hash)