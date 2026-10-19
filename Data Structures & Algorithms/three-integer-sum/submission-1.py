class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res ={}
        nums = sorted(nums)
        for i in range(size-2):
            left = i+1
            right = size-1
            while left < right:
                _sum = nums[i] + nums[left] + nums[right] 
                if _sum == 0:
                    res[tuple([nums[i],nums[left],nums[right]])]=([nums[i],nums[left],nums[right]])
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
        return list(res.values())