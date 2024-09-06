from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p, q = 0, len(nums) - 1

        while p <= q:
            mid = (p + q) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] < target:
                p = mid + 1
            else:
                q = mid - 1

        return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]

    for i in nums:
        index = Solution().search(nums=nums, target=i)
        print("Number ", i, " Index ", index)

    print(Solution().search(nums=[-1, 0, 3, 5, 9, 12], target=13))
