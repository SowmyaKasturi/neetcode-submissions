class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(nums)
        print(list(set(nums)))
        return sorted(nums) != sorted(list(set(nums)))