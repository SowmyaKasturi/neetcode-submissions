class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {'[':']', '{':'}', '(':')'}
        stack = []
        for char in s:
            if char in valid_pairs:
                stack.append(char)
            elif stack and char == valid_pairs[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack
