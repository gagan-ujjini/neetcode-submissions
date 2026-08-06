class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = dict()
        for i in s:
            if i not in arr:
                arr[i] = 1
            else:
                arr[i] += 1
        for j in t:
            if j not in arr:
                arr[j] = 1
            else:
                arr[j] -= 1
        
        for key, val in arr.items():
            if val != 0:
                return False
        return True
