from typing import List
from collections import Counter

class Solution:
    def check(self, values):
        v = Counter(values)
        for jj in v:
            if jj == ".":
                continue
            if v[jj] > 1:
                return False
        
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for i in board:
            # first check row
            if not self.check(i):
                return False


        # now check column
        for i in range(len(board)):
            cols = [board[j][i] for j in range(len(board))]
            if not self.check(cols):
                return False


        # check 3*3 blocks
        row_start = 0
        row_end = 3
        col_start = 0
        col_end = 3
        
        for i in range(9):
            check_box = []
            for j in range(row_start,row_end):
                for k in range(col_start,col_end):
                    check_box.append(board[j][k])

            if not self.check(check_box):
                return False
        
            col_start+=3
            col_end+=3
            if col_end > 9:
                col_start = 0
                col_end = 3
                row_start+= 3
                row_end += 3
        
        return True



if __name__ == '__main__':
    sol = Solution()
    s = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    print(sol.isValidSudoku(s))