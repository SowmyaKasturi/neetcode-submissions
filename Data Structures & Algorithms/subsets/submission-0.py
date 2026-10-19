class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        length = len(nums)
        def dfs(index, subset):
            if index == length:
                result.append(subset[:])
                return
            subset.append(nums[index])
            dfs(index+1, subset)
            subset.pop()
            dfs(index+1,subset)
        dfs(0, [])
        return result