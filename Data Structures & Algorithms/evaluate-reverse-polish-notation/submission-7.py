class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if token == '+':
                sym1 = int(stack.pop())
                sym2 = int(stack.pop())
                stack.append(sym1 + sym2)
            elif token == '-':
                sym2 = int(stack.pop())
                sym1 = int(stack.pop())
                stack.append(sym1 - sym2)
            elif token == '/':
                sym2 = int(stack.pop())
                sym1 = int(stack.pop())
                stack.append(int(sym1 / sym2))
            elif token == '*':
                sym1 = int(stack.pop())
                sym2 = int(stack.pop())
                stack.append(sym1 * sym2)
            else: 
                stack.append(token)
        return stack[-1]
            