class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            t_str = tuple(sorted(i))
            if t_str not in anagrams:
                anagrams.setdefault(t_str,[])
            anagrams[t_str].append(i)
        print()
        return anagrams.values()
