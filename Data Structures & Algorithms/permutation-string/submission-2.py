class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window_size = len(s1)

        s1_count = [0] * 26
        window_count = [0] * 26

        # Build frequencies for s1 and the first window of s2
        for index in range(window_size):
            s1_character = ord(s1[index]) - ord('a')
            window_character = ord(s2[index]) - ord('a')

            s1_count[s1_character] += 1
            window_count[window_character] += 1

        # Check the first window
        if s1_count == window_count:
            return True

        # Slide the window through the rest of s2
        for right in range(window_size, len(s2)):
            entering_character = ord(s2[right]) - ord('a')
            window_count[entering_character] += 1

            left = right - window_size
            leaving_character = ord(s2[left]) - ord('a')
            window_count[leaving_character] -= 1

            if s1_count == window_count:
                return True

        return False