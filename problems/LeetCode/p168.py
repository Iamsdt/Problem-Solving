class Solution:
    def convertToTitle(self, c: int) -> str:
        s = ""
        while (c>0):
            c -= 1
            s = chr(65+c % 26) + s
            c //= c // 26
        return s


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.convertToTitle(25))