class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        border_cells = set()
        for r in range(rows):
            border_cells.add((r,0) )
        for c in range(cols):
            border_cells.add((0,c))
        for r in range(rows):
            border_cells.add((r,cols-1))
        for c in range(cols):
            border_cells.add((rows-1,c))
        print(border_cells)
        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != "O":
                return
            board[i][j] = "#"
            dfs(i, j+1)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i-1,j)
        
        for _ in border_cells:
            print(_)
            i,j = _
            if board[i][j] == "O":
                dfs(i,j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "#":
                    board[i][j] = "O"
