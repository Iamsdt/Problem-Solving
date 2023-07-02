from collections import Counter
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(values):
            di = Counter(values)
            for j in di:
                # not filled
                if j == ".":
                    continue
                elif di[j] > 1:
                    return False

            return True

        # first check all the rows
        for i in board:
            if not check(i):
                return False

        # check cols
        for i in board:
            cols = [board[j][i] for j in range(len(board))]
            if not check(cols):
                return False

        # check 3*3 blocks
        row_start, row_end = 0, 3
        col_start, col_end = 0, 3
        for i in range(9):
            checkbox = [board[j][k] for j in range(
                row_start, row_end) for k in range(col_start, col_end)]
            # fill the data
            if not check(checkbox):
                return False

            # now updated params
            col_start += 3
            col_end += 3
            if col_end > 9:
                col_start = 0
                col_end = 3
                row_start += 3
                row_end += 3

        return True
