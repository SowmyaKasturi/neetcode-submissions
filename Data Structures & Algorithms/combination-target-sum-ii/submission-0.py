class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        def dfs(i, stack, target_sum):
            if target_sum == target:
                res.add(tuple(stack[:]))
                return
            if i == len(candidates) or target_sum > target:
                return
            stack.append(candidates[i])
            dfs(i+1, stack,target_sum+candidates[i])
            stack.pop()
            dfs(i+1, stack, target_sum)
        dfs(0,[],0)
        return [list(combination) for combination in res]