class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        low, high = 0, (row*col)-1

        while low <= high:
            mid = low + (high-low)//2
            #IMPORTANT: To find mid in the matrix
            r = mid//col
            print(r)        
            c = mid%col
            print(c)         

            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                low = mid + 1
            else:
                high = mid - 1
        return False

#T: O(log(m*n))
#S: O(1)