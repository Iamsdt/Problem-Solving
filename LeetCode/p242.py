# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
    def isAnagram2(self, s: str, t: str) -> bool:
        # sorted complexity logN, so total nlogN
        return sorted(s) == sorted(t)