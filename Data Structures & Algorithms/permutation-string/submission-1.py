class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        sorted_s1 = sorted(s1)  #O(n log n)
        window_size = len(s1)

        for start in range(len(s2) - window_size + 1): #m - n + 1
            current_window = s2[start:start + window_size]

            if sorted(current_window) == sorted_s1: #O(nlogn)
                return True

        return False

#Time = O((m - n + 1) × n log n) which simplifies to O(m × n log n)
#Space = extra space comes from sorting n characters so O(n)