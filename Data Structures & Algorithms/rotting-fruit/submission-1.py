from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        while queue and fresh > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                flag = 0
                for dx, dy in directions:
                    row = i + dx
                    col = j + dy
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append((row,col))
                        fresh -= 1
            count += 1

        return count if fresh == 0 else -1