class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        # perms = list("".join(_) for _ in permutations(s1))
        # for i in perms:
        #     if i in s2:
        #         return True
        # return False
        if s1 in s2:
            return True
        i = 0
        j = 0
        freq = Counter(s1)
        print(freq)
        for i in range(len(s2)):
            print(Counter(s2[i: i + len(s1)]))
            if Counter(s2[i:i + len(s1)]) == freq:
                return True
        return False