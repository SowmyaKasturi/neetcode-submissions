class Solution:
    def pivotIndex(self,nums):
        total = sum(nums)     # total sum
        left_sum = 0

        for i, num in enumerate(nums):
            # right_sum = total - left_sum - current element
            
            if left_sum == total - left_sum-num:
                return i
            
            left_sum += num
        return -1