# class Solution:
#     def climbStairs(self, n: int) -> int:
#         count = 0
#         def recurse( temp):
#             if temp >= n:
#                 return temp == n 
#             return recurse(temp + 1) + recurse(temp + 2)
#         return recurse(0)
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)