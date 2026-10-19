class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        anagram = {}
        for i in strs:
            _key = "".join(sorted(i))
            anagram.setdefault(_key, [])
            anagram[_key].append(i)
        return list(anagram.values())