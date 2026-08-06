class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force
        # maxArea = 0
        # for i in range(len(heighs)):
        #     for j in range(i+1, len(heights)):
        #         area = min(heights[i], heights[j]) * (j-i)
        #         maxArea = max(area, maxArea)
        # return maxArea

        #optimal
        maxArea = 0
        l, r = 0, len(heights)-1
        while l < r:
            area = min(heights[l], heights[r])*(r-l)
            maxArea = max(area, maxArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea

#T: O(n)
#S: O(1)