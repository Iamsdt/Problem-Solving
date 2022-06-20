class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = len(matrix[0])- 1
        while r <= len(matrix)- 1 and c >= 0:
            print(matrix[r][c])
            if matrix[r][c] == target:
                return True
            elif target > matrix[r][c]:
                r += 1
            elif target < matrix[r][c]:
                c -= 1
        return False