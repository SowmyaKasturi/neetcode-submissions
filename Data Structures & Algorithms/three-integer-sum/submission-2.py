class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []
        nums = sorted(nums)
        for i in range(size-2):
            left = i+1
            right = size-1
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            while left < right:
                _sum = nums[i] + nums[left] + nums[right] 
                if _sum == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif _sum > 0:
                    right -= 1
                else:
                    left += 1
             
            # for j in range(i+1,size):
            #     for k in range(j+1, size):
            #         if nums[i] + nums[j] + nums[k] == 0:
            #             res[tuple(sorted([nums[i],nums[j],nums[k]]))]=([nums[i],nums[j],nums[k]])
        return res