class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            result[i] = product
        return result

#T: O(n^2) since we have two for loops
#S: O(n) if we count the result array else O(1) if we exclude
# the result array