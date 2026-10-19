class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # start at first position go to the next line and 
        # find cirrect position for the queen 
        # and keep conitnuting once reached the end 
        # if there are no four queens go bavk to parent an d take next position continue this 

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
                print("KKKKKK")
                return
            for col in range(n):
                if is_valid(matrix, row, col):
                    matrix[row][col] = "Q"
                    dfs(matrix, row+1)
                    matrix[row][col] = "."
            

    
        matrix = [["." for _ in range(n)] for _ in range(n)]
        res = []
        dfs(matrix, 0)
        return res
        