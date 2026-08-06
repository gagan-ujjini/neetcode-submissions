class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the separator #
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # Extract word using its length
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            i = j + 1 + length

        return res