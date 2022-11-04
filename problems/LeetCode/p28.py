
# Hacking solution: But does't work in real world
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)

        return -1


# Lets implement KMP (Knuth, morris and pratt)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.strStr(haystack="aaa",needle="bb"))