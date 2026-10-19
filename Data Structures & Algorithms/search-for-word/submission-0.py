from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        def dfs(row, col, index):
            if index == len(word):  # Base case: found full word
                return True
            if not (0 <= row < rows and 0 <= col < cols) or board[row][col] != word[index]:
                return False

            # Mark as visited by modifying the board temporarily
            temp = board[row][col]
            board[row][col] = '#'  

            # Explore all four directions
            for dr, dc in directions:
                if dfs(row + dr, col + dc, index + 1):
                    return True
            
            # Restore the board (backtrack)
            board[row][col] = temp
            return False

        # Start DFS from all positions matching word[0]
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and dfs(row, col, 0):
                    return True
        return False
