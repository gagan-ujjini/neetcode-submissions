class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        l = 0

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1

            while (r-l+1) - max(count.values()) > k:    #when diff btw window size and max char count > k shrink window
                #res = max(res, r-l+1)         #cannot be inside as there could be arra where given condition doesnt meet
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res

#T: O(n) since it is fixed alphabet solution
#S: O(26)~O(1) since hashmap stores one entry per distinct character.