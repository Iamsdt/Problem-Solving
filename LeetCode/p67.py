class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = bin(int(a, 2) + int(b, 2))
        return sum[2:]


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.addBinary(a="101", b="11"))