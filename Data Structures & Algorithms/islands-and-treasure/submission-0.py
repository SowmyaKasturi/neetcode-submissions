from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        INF=2147483647
    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        while queue:
            i,j = queue.popleft()
            for dx, dy in directions:
                row = i + dx
                col = j + dy
                if 0 <= row < rows and 0 <= col < cols and grid[row][col] == INF:
                    grid[row][col] = grid[i][j] + 1
                    queue.append((row,col))

                            