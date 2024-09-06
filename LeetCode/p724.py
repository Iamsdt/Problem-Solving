from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        total = sum(nums)
        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            left += nums[i]

        return -1

if __name__ == "__main__":
    print(Solution().pivotIndex([1,7,3,6,5,6]))
    print(Solution().pivotIndex([1,2,3]))
    print(Solution().pivotIndex([2,1,-1]))
