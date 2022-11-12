import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log(n, 4).is_integer()


if __name__ == '__main__':
    print(Solution().isPowerOfFour(-2147483648))
    print(Solution().isPowerOfFour(2147483648))
    print(Solution().isPowerOfFour(4))
    print(Solution().isPowerOfFour(1))
    print(Solution().isPowerOfFour(12))
    print(Solution().isPowerOfFour(256))
    print(Solution().isPowerOfFour(81))
