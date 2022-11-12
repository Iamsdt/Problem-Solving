import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        b = dividend / divisor
        last = math.modf(b)[0]
        ans = b - last
        if ans <= -2 ** 31:
            return -2 ** 31
        elif ans >= 2 ** 31:
            return 2 ** 31 - 1

        return int(ans)


if __name__ == "__main__":
    print(Solution().divide(-2147483648, -1))
