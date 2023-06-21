from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        rs = Counter(s)
