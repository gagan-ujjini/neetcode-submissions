class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # if openN == n return 
        # if openN < n add open
        # if close < open add close

        result = []
        stack = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                return result.append("".join(stack))
            
            if openN < n:
                stack.append("(")
                print(openN+1, closedN)
                backtrack(openN+1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                print(openN, closedN+1)
                backtrack(openN, closedN+1)
                stack.pop()

        backtrack(0,0)
        return result