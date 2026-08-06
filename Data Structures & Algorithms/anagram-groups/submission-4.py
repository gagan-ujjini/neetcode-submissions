class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            array = [0]*26
            for char in s:
                idx = ord(char) - ord('a')
                array[idx] += 1
            hashmap[tuple(array)].append(s)

        return [val for val in hashmap.values()]

#T: (m * n)
#S: O(m * n)