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


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
