class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        res = set()
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    res.add((row,col))
        for row, col in res:
            for c in range(cols):
                matrix[row][c] = 0
            for r in range(rows):
                matrix[r][col] = 0

