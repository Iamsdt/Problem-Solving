class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)

        return -1



if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.strStr(haystack="aaa",needle="bb"))