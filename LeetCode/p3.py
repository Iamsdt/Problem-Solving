# Sliding Window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[l])
                l += 1

            window.add(s[i])
            res = max(res, i - l + 1)

        return res


# 3. Longest Substring Without Repeating Characters3. Longest Substring Without Repeating Characters
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # check length first
        if len(s) <= 1:
            return len(s)

        # create a dict to track records or not
        di = {}
        # this will hold max length
        max_length = 0
        # create an start point
        start = 0

        for i in range(len(s)): # O(n)
            if s[i] in di and start <= di[s[i]]: #O(1)
                # that means, it's already seen
                # so increase the start
                start = di[s[i]] + 1

            else:
                length = i - start + 1
                # get the max value
                max_length = max(length, max_length)

            # save current character into dict
            di[s[i]] = i

        return max_length

    # complexity: O(n)


# Approach 1: Brute Force
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):  # o(n)
            for j in range(i, len(s)):  # o(n)
                if self.allUnique(s, i, j):  # o(n) all unique use loop
                    ans = max(ans, j-1)

        return ans

    def allUnique(self, sub: str, start: int, end: int) -> bool:
        values = set()
        for i in range(start, end):
            char = sub[i]

            if char in values:
                return False

            set.add(char)

        return True

    # total complexity O(N) * O(N) * O(N) = O(N^3)
