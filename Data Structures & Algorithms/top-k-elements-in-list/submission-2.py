class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        result = []
        for num in nums:
            if num not in mydict:
                mydict[num] = 1
            else:
                mydict[num] += 1
        sorted_dict = sorted(mydict.items(), key = lambda item: item[1], reverse=True)
        
        for (key, val) in sorted_dict:
            if k != 0:
                result.append(key)
                k -= 1
        return result