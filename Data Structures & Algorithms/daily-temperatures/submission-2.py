class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        result = [0] * size
        stack = []
        for i in range(size):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]]=(i-stack[-1])
                stack.pop()
            stack.append(i)
        return result
            