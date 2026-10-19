class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _duplicate = set()
        for i in nums:
            if i in _duplicate:
                return True
            _duplicate.add(i)
        return False