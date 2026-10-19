class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        length = len(nums)
        def dfs(index, subset):
            if index == length:
                result.add(tuple(subset[:]))
                return
            subset.append(nums[index])
            dfs(index+1, subset)
            subset.pop()
            dfs(index+1, subset)
        nums.sort()
        dfs(0,[])
        return [list(s) for s in result]
