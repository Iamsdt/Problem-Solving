# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pyparsing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for i in nums:
            temp = max(rob1 + 1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
