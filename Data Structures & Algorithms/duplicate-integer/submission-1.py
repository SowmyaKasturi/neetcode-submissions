class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _hash = {}
        for i in nums:
            if i not in _hash:
                _hash[i] = 1
            else:
                return True
        return False