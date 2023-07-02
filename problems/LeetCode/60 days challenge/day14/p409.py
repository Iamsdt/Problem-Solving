from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        counter = Counter(s)

        addedOne = False
        final = ''

        for c, freq in counter.items():
            print(c, freq, freq % 2)
            if freq % 2:
                if not addedOne:
                    ans += freq
                    final += c * (freq)
                    addedOne = True
                else:
                    ans += freq-1
                    final += c * (freq-1)

            else:
                final += c * freq
                ans += freq

        print(final)
        return ans


if __name__ == "__main__":
    print(Solution().longestPalindrome("abccccdd"))
