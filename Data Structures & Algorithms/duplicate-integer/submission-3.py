class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track_duplicate = dict()
        for i in nums:
            if track_duplicate.get(i):
                return True
            track_duplicate[i] = 1
        return False