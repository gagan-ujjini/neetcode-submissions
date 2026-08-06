class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        sorted_s1 = sorted(s1)
        window_size = len(s1)

        for start in range(len(s2) - window_size + 1):
            current_window = s2[start:start + window_size]

            if sorted(current_window) == sorted_s1:
                return True

        return False