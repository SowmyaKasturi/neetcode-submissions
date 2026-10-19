class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for row in board:
        #     row_set = set()
        #     for value in row:
        #          if value != ".":
        #               if value in row_set:
        #                    return False
        #               row_set.add(value)
        # for row in range(9):
        #     col_set = set()
        #     for col in range(9):
        #         value = board[col][row]
        #         if value != ".":
        #             if value in col_set:
        #                 return False
        #             col_set.add(value)
        
        # for i in range(0,9,3):
        #     for j in range(0,9,3):
        #         grid_set = set()
        #         for k in range(i, i+3):
        #             for l in range(j, j+3):
        #                 value = board[k][l]
        #                 if value != ".":
        #                     if value in grid_set:
        #                         return False
        #                     grid_set.add(value)
        # return True
        for i in range(9):
            row_set = set()
            col_set = set()
            subgrid_set = set()
            for j  in range(9):
                #for each row
                value = board[i][j]
                if  value != ".":
                    if value in row_set:
                        return False
                    row_set.add(value)
                #for each column
                value = board[j][i]
                if value != ".":
                    if value in col_set:
                        return False
                    col_set.add(value)
                
                #for each grid
                grid_row = (i//3) * 3 + j // 3
                grid_col = (i % 3) * 3 + j % 3
                value = board[grid_row][grid_col]
                if value != ".":
                    if value in subgrid_set:
                        return False
                    subgrid_set.add(value)
        return True
