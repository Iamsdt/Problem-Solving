from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(
            nums[-1] * nums[-2] * nums[-3],
            nums[0] * nums[1] * nums[-1],
        )

    def maximumProduct2(self, nums: List[int]) -> int:
        max1 = max2 = max3 = float("-inf")
        min1 = min2 = float("inf")

        for num in nums:
            if num > max1:
                max3, max2, max1 = max2, max1, num
            elif num > max2:
                max3, max2 = max2, num
            elif num > max3:
                max3 = num

            if num < min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumProduct([1, 2, 3]))  # Output: 6
    print(sol.maximumProduct([1, 2, 3, 4]))  # Output: 24
    print(sol.maximumProduct([-1, -2, -3]))  # Output: -6
    print(sol.maximumProduct([-1, -2, -3, 0]))  # Output: 0
    print(sol.maximumProduct([-100, -98, -1, 2, 3, 4]))  # Output: 39200
