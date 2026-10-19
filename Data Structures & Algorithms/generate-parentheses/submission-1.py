class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
            size=2*n
            result = []
            def generate_permutations(stack, open_c, close_c):
                if len(stack) == size:
                    return result.append("".join(stack))
                if open_c > close_c:
                    stack.append(")")
                    close_c += 1
                    generate_permutations(stack, open_c, close_c)
                    stack.pop()
                    close_c -= 1
                if open_c < n:
                    stack.append("(")
                    open_c += 1
                    generate_permutations(stack, open_c, close_c)
                    stack.pop()
                    open_c -= 1
            print(generate_permutations([],0,0))
            return result
            