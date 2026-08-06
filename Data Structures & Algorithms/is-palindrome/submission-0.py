class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for i in range(len(s)):
            if s[i].isalnum():
                result.append(s[i].lower())
        
        if "".join(result) == "".join(result[::-1]):
            return True
        else:
            return False