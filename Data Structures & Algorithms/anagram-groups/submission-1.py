class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for s in strs:                              #O(n)
            sorted_string = "".join(sorted(s))      #O(nlogn)
            dict[sorted_string].append(s)
        
        result = []
        for key, val in dict.items():               #O(n)
            result.append(val)
        return result

#T: O(nlogn)
#S: O(n)