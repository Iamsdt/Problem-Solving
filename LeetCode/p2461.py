from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        window = set()
        start = 0

        for i, v in enumerate(nums):
            window.add(v)

            if (i - start + 1) != k:
                continue

            # we have a full window
            # but window size need to be same as k
            if len(window) == k:
                res = max(res, sum(window))

            window.remove(nums[start])
            start += 1

        return res




if __name__ == "__main__":
    print(Solution().maximumSubarraySum([1,5,4,2,9,9,9], k=3))
    print(Solution().maximumSubarraySum([4, 4, 4], k=3))
    print(Solution().maximumSubarraySum([1,1,1,7,8,9], k=3))