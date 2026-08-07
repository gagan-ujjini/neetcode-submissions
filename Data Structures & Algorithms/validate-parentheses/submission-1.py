class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif stack and hashmap[char] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return False if stack else True
        
    #T: O(n)
    #S: O(n) worst case if all the bracketts are opening bracketss