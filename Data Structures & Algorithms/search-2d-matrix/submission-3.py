class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, (rows*cols)-1

        while low <= high:
            mid = low + (high-low)//2
            r = mid//cols
            c = mid % cols
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                high -= 1
            else:
                low += 1
        return False