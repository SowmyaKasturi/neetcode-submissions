class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(-1,0), (0,1),(1,0),(0,-1)]
        visited_grid = set()
        islands = 0
        def bfs(row,col):
            queue = deque()
            queue.append((row, col))
            visited_grid.add((row,col))
            while queue:
                row, col = queue.popleft()
                for i,j in directions:
                    nr = row + i
                    nc = col + j
                    if 0 <= nr < m and 0<= nc < n and grid[nr][nc] == "1"\
                    and (nr,nc) not in visited_grid:
                            visited_grid.add((nr, nc))
                            queue.append((nr, nc))
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row,col) not in visited_grid:
                    bfs(row,col)
                    islands += 1 
        return islands