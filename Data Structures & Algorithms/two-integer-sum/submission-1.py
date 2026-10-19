class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _hash = {}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement not in _hash:
                _hash.setdefault(nums[i],i)
            else:
                return [_hash[complement], i]
        return [-1,-1]