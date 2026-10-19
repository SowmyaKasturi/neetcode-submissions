class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
            size=2*n
            result = []
            def generate_permutations(stack, open_c, close_c):
                if len(stack) == size:
                    result.append("".join(stack))
                    return 
                if open_c > close_c:
                    stack.append(")")
                    generate_permutations(stack, open_c, close_c + 1)
                    stack.pop()
                if open_c < n:
                    stack.append("(")
                    generate_permutations(stack, open_c+1, close_c)
                    stack.pop()
            print(generate_permutations([],0,0))
            return result
            