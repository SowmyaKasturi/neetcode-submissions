class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        row = left
        mid=0
        while left <= right:
            mid = (right+left) // 2
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                break
        row=(right+left) // 2
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            print(mid)
            mid = (right+left) // 2
           
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False