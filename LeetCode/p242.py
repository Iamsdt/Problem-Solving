# Copyright (c) 2022 Shudipto Trafder
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from collections import Counter

class Solution:
    def isAnagram3(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
    def isAnagram2(self, s: str, t: str) -> bool:
        # sorted complexity logN, so total nlogN
        return sorted(s) == sorted(t)
    

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Create a dictionary to count characters in s
        count = {}

        # Count each character in s
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Decrement the count for each character in t
        for char in t:
            if char in count:
                count[char] -= 1
                if count[char] == 0:
                    del count[char]
            else:
                return False


        return len(count) == 0