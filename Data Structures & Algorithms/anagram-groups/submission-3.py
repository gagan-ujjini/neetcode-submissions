class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        #O(n * klogk) where k is max length of a string
        for s in strs:                              #O(n)
            sorted_string = "".join(sorted(s))      #O(klogk)
            dict[sorted_string].append(s)

        result = []
        for key, val in dict.items():               #O(n)
            result.append(val)
        return result

#T: O(n * klogk)
#S: O(n*k) because we are storing a dictionary upto n keys and 
# each string is stored once(Each string length = k)