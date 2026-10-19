from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        res = []
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Move left to right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1  # Move boundary down

            # Move top to bottom
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1  # Move boundary left

            if top <= bottom:
                # Move right to left
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1  # Move boundary up

            if left <= right:
                # Move bottom to top
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1  # Move boundary right

        return res
