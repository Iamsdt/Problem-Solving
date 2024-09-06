from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        ans = [[0 for _ in range(c)] for _ in range(r)]
        
        # print(temp)
        row, col = 0, 0
        for line in mat:
            for element in line:
                ans[row][col] = element
                if col == c - 1:
                    row += 1
                    col = 0
                else:
                    col += 1
        return ans