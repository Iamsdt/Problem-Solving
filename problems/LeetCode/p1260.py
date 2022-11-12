from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        
        def val_to_pos(v):
            return [v//c, v%r]

        res = [[0] * c for i in range(r)]
        for i in range(r):
            for j in range(c):
                pos = i*c + j
                pos += k
                new_pos = pos % (r*c)
                new_r, new_c = val_to_pos(new_pos)
                res[new_r][new_c] = grid[i][j]

        return res