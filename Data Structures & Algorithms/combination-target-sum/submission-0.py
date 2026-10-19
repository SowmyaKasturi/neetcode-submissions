class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def find_target_sum(index, stack, target_sum):
            if target_sum == target:
                res.append(stack[:])
                return
            if index >= len(nums) or target_sum > target:
                return
            stack.append(nums[index])
            find_target_sum(index, stack, target_sum + nums[index])
            stack.pop()
            find_target_sum(index+1, stack, target_sum)
        
        
        find_target_sum(0, [], 0)
        return res