class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        res = []
        i = 0
        while i < (length-k+1):
            res.append(max(nums[i:i+k]))
            i += 1
        return res
        