import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols  = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    a, b = row+dr, col+dc
                    if a in range(rows) and b in range(cols) and grid[a][b] == "1" and (a, b) not in visited:
                        q.append((a, b))
                        visited.add((a,b))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
                    
        return islands