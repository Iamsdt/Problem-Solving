from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        value = -1
        for i in nums:
            if i * -1 in nums:
                value = max(value, abs(i))

        return value


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxK([-1, 2, -3, 3]))
    print(s.findMaxK([-1, 10, 6, 7, -7, 1]))
    print(s.findMaxK([-10, 8, 6, 7, -2, -3]))
