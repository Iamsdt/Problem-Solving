from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use counter or sorted
        return s[::-1] == t
