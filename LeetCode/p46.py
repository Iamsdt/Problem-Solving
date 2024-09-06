from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(permutation, remaining):
            # if its same as nums, so its done
            if len(permutation) == len(nums):
                res.append(permutation[:])
                return

            for i, v in enumerate(remaining):
                permutation.append(v)

                next_remaining = remaining[0:i]+remaining[i+1:]
                backtrack(permutation, next_remaining)
                permutation.remove(v)

        backtrack([], nums)
        return res


if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
