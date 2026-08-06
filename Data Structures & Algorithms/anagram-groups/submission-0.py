class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for s in strs:
            sorted_string = "".join(sorted(s))
            dict[sorted_string].append(s)
        
        result = []
        for key, val in dict.items():
            result.append(val)
        return result
