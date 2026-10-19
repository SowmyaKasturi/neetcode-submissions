class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res ={}
        for i in range(size):
            for j in range(i+1,size):
                for k in range(j+1, size):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res[tuple(sorted([nums[i],nums[j],nums[k]]))]=([nums[i],nums[j],nums[k]])
        return list(res.values())