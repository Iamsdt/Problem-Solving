"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right-left-1

        start, end = 0, 0
        for index in range(len(s)):
            even = expand(s, index, index+1)
            odd = expand(s, index, index)
            length = max(even, odd)
            print(length)
            if length > (end-start):
                start = index - (length-1)//2
                end = index + length//2
        return s[start:end+1]


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.longestPalindrome("a"))
