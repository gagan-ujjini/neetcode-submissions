class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numsSet = set()
        for i in nums:
            if i not in numsSet:
                numsSet.add(i)
            else:
                return i