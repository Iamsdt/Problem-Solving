# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in matrix:
            print(i)



nums = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(nums)
print(nums)