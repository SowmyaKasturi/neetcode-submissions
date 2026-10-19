class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = []
        if not nums:
            return 0
        for i in nums:
            seen = set()
            seen.add(i)
            if i - 1 in nums:
                continue
            while i + 1 in nums:
                seen.add(i+1)
                i += 1
            res.append(len(seen))
        return max(res)
        