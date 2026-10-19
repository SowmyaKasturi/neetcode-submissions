class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = len(nums)
        prefix = [1] * s
        for i in range(1,s):
            prefix[i] = prefix[i-1] * nums[i-1]
        suffix = 1
        for i in range(s-1,-1,-1):
            prefix[i] *= suffix
            suffix *= nums[i]
        return prefix