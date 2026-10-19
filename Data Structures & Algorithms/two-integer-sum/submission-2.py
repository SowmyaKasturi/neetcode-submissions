class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res =  {}
        for i in range(len(nums)):
            _diff = target - nums[i]
            if nums[i] in res:
                return [res[nums[i]], i]
            res[_diff] = i