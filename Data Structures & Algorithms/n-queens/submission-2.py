class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def is_valid(matrix, row, col):
            for i in range(row):
                if matrix[i][col] == "Q":
                    return False
            
            i,j = row -1, col-1
            while i >= 0 and j >= 0:
                if matrix[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            
            i,j = row-1, col+1
            while j < n and i >= 0:
                if matrix[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True
            
        def dfs(matrix, row):
            if row == n:
                res.append(["".join(i) for i in matrix])
                return
            for col in range(n):
                if col in col_set or row+col in anti_diag or row-col in main_diag:
                    continue
                # if is_valid(matrix, row, col):
                matrix[row][col] = "Q"
                col_set.add(col)
                anti_diag.add(row+col)
                main_diag.add(row-col)
                dfs(matrix, row+1)
                matrix[row][col] = "."
                col_set.remove(col)
                anti_diag.remove(row+col)
                main_diag.remove(row-col)

    
        matrix = [["." for _ in range(n)] for _ in range(n)]
        res = []
        col_set = set()
        main_diag = set()
        anti_diag = set()
        dfs(matrix, 0)
        return res
        