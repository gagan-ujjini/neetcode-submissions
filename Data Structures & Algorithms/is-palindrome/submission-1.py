class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for char in s:
            if char.isalnum():
                result.append(char)
        
        result = "".join(result).lower()
        print(result)
        return result == result[::-1]