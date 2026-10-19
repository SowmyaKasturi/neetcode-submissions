class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        if k > length:
            return []
        res = []
        i = 0
        while i < (length-k+1):
            max_v = -1
            for j in range(i, i+k):
                max_v = max(max_v, nums[j])
            res.append(max_v)
            i += 1
        return res

        


        