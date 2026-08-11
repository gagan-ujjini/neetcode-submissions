class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            k = (low+high)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            
            if hours > h:
                low = k + 1 # k is too slow
            else:
                high = k - 1 # k works, but maybe a smaller speed also works

        return low

#T: O(N * log(M)) where N is number of piles and M is max number of bananas in the pile