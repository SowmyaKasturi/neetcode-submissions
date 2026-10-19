class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_n = len(nums)
        sum_n = sum(nums)
        sum_till_max = (max_n * (max_n+1))//2
        return sum_till_max-sum_n