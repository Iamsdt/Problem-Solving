# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pyparsing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        ods = 0
        even = 0

        for i, v in enumerate(nums):
            if i % 2 == 0:
                ods += v
            else:
                even += v
        
        return max(ods, even)