class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result  = []
        for i in range(len(nums)-k+1):
            print(i)
            max_i = float('-inf')
            for j in range(k):
                max_i = max(max_i, nums[i+j])
            result.append(max_i)
        return result