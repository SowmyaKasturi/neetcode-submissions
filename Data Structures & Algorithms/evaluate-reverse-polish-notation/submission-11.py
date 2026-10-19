class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ["+","-","*","/"]:
                stack.append(int(i))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if i == "+":
                    stack.append(op2+op1)
                elif i == "-":
                    stack.append(op2-op1)
                elif i == "*":
                    stack.append(op2*op1)
                else:
                    stack.append(int(op2/op1))
        return stack[-1]