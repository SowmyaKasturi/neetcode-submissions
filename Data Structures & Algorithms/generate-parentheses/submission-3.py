from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate_permutations(stack, open_c, close_c):
            if len(stack) == 2 * n:
                result.append(stack)
                return  

            if open_c < n:  
                generate_permutations(stack + "(", open_c + 1, close_c)  

            if close_c < open_c:  
                generate_permutations(stack + ")", open_c, close_c + 1)  

        generate_permutations("", 0, 0)
        return result
