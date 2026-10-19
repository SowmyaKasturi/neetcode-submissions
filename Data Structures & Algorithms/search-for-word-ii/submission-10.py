class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        rows = len(board)
        cols = len(board[0])
        directions = [ (0,1), (1,0), (0,-1),(-1,0)]
        ch_map = {}
        res = set()
        
        
        def dfs(i,j,index, word, visited):
            visited.add((i,j))
            if index == len(word):
                return True
            for r,c in directions:
                row = i+r
                col = j+c
                if 0 <= row < rows and 0 <= col < cols and board[row][col] == word[index] \
                    and  (row,col) not in visited  and dfs(row,col, index+1, word, visited):
                    return True
            visited.remove((i,j))
            return False

        for word in words:
            for i in range(rows):
                for j in range(cols):
                    if board[i][j] == word[0] and dfs(i,j,1, word, set()):
                            res.add(word)
        return list(res)

