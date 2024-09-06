from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        ans = 0
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == row or c == col:
                return 0
            elif grid[r][c] == 0 or (r,c)in visit:
                return 0
            
            # now add this island into visited
            visit.add((r,c))    
            return (1+ dfs(r+1, c)
            + dfs(r-1, c)
            + dfs(r, c+1)
            + dfs(r, c-1))


        for r in range(row):
            for c in range(col):
                ans = max(ans, dfs(r, c))

        return ans
