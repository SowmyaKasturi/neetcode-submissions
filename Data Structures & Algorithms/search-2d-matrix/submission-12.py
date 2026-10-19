class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        row = -1
        while low <= high:
            mid = (high+low)//2
            if matrix[mid][0] <= target <=matrix[mid][-1]:
                row = mid
                low = 0
                high = len(matrix[0]) - 1
                while low <= high:
                    mid = (high+low) // 2
                    if target == matrix[row][mid]:
                        return True
                    elif target < matrix[row][mid]:
                        high = mid-1
                    else:
                        low = mid+1
                break
            elif target < matrix[mid][0]:
                high =mid- 1
            else:
                low = mid+ 1
        if row == -1:
            return False
        return False

