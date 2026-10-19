class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            left = 0
            right = len(i)-1
            while left <= right:
                mid = (right+left) // 2
                print(left,right,mid)
                if i[mid] == target:
                    return True
                elif i[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False