from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix[0])
        memo = [[None for _ in range(n)] for _ in range(n)] 
        min_count = float('inf')


        def dfs(i,j):
            if i >= len(matrix):
                return 0
            if memo[i][j]:
                return memo[i][j]
            memo[i][j]=matrix[i][j] + min(
                    dfs(i+1,j),
                    dfs(i+1,max(0,j-1)), 
                    dfs(i+1,min(len(matrix)-1,j+1))
                )
            return memo[i][j]

        
        for j in range(n):
            min_count=min(min_count,dfs(0,j))
        return min_count