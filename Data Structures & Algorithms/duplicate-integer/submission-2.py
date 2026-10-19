class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _hash = set()
        for i in nums:
            if i in _hash:
                return True
            _hash.add(i)
        return False