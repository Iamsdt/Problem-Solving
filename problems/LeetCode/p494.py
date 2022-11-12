class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            one, two = one + two, one

        return one

    def climbStairs2(self, n: int) -> int:
        if n < 3:
            return n

        return self.climbStairs2(n - 1) + self.climbStairs2(n - 2)


if __name__ == "__main__":
    print(Solution().climbStairs(4))
    print(Solution().climbStairs2(4))
