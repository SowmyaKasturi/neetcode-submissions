class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        anagram_hash = {}

        for i in strs:
            sort_i = "".join(sorted(i))
            anagram_hash.setdefault(sort_i,[])
            anagram_hash[sort_i].append(i)
        return list(anagram_hash[i] for i in anagram_hash)