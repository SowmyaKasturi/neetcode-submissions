class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _hash = {}
        for i in range(len(nums)):
            complement = target-nums[i]
            if nums[i] not in _hash:
                _hash.setdefault(complement,i)
            else:
                return [_hash[nums[i]], i]
        return [-1,-1]