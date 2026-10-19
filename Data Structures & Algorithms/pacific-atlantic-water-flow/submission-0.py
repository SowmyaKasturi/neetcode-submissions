from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])    
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def bfs(starts):
            queue = deque(starts)
            visited = set(starts)
            while queue:
                i,j = queue.popleft()
                for dx,dy in directions:
                    nr,nc = i+dx, j+dy
                    if 0 <= nr < rows and 0 <= nc < cols and\
                    (nr,nc) not in visited and\
                     heights[i][j] <= heights[nr][nc]:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            return visited

        pacific_start = [(0,c) for c in range(cols)]+[(r,0) for r in range(rows)]
        atlantic_start = [(rows-1,c) for c in range(cols)] + [(r,cols-1) for r in range(cols)]
        return list( bfs(pacific_start) & bfs(atlantic_start))