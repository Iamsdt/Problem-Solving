from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = set(nums)
        res = 0
        for i in nums:
            if (i - 1) not in data:
                length = 1
                while (i + length) in data:
                    length += 1
                res = max(res, length)

        return res


if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(Solution().longestConsecutive(nums))
