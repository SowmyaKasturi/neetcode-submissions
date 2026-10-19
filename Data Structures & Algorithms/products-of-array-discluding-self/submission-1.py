import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = len(nums)
        suffix = [0] * s
        prefix = [0] * s
        suffix[-1] = 1
        prefix[0] = 1
        for i in range(1,s):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(s-2, -1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        for i in range(s):
            nums[i] = prefix[i] * suffix[i]
        return nums