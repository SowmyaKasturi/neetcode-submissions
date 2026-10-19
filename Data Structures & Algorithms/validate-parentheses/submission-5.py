class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        h = {']':'[', '}':'{', ')':'('}
        for i in s:
            if i in h.values():
                stack.append(i)
            elif i in h:
                if not stack or stack[-1] != h[i]:
                    return False
                stack.pop()
            else:
                return False
        return not stack