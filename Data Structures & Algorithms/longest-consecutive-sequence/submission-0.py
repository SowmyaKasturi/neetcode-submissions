class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_count = 0
        for i in set_nums:
            count = 1
            if i-1 in set_nums:
                continue
            while i+1 in set_nums:
                count += 1
                i += 1
            max_count  = max(max_count,count)
        return max_count