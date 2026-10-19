class Solution:
    from collections import deque
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited_grid = set()
        directions = [(-1,0), (0,1),(1,0), (0,-1)]
        def bfs(row, col):
            queue = deque([(row,col)])
            visited_grid.add((row,col))
            land_area = 1
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]\
                        and (nr,nc) not in visited_grid:
                        queue.append((nr,nc))
                        visited_grid.add((nr,nc))
                        land_area += 1
            return land_area
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] and (row,col) not in visited_grid:
                    max_area = max(bfs(row,col), max_area)
        return max_area


