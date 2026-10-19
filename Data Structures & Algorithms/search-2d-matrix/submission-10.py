class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        row = 0
        while low <= high:
            mid = (high+low)//2
            if target in matrix[mid]:
                row = mid
                break
            elif target < matrix[mid][0]:
                high -= 1
            else:
                low += 1
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
        return False

