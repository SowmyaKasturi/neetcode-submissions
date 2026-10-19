import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(math.prod(nums[:i]+nums[i+1:]))
        return output