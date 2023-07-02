from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        p, q = 0, len(nums) - 1

        res = []

        for i in range(len(nums)):
            value = nums[i]
            # filter
            if i > 0 and value == nums[i - 1]:
                continue

            # run binary search
            p, q = i + 1, len(nums) - 1
            while p < q:
                three_sum = value + nums[p] + nums[q]
                if three_sum < 0:
                    p += 1
                elif three_sum > 0:
                    q -= 1
                else:
                    res.append([nums[i], nums[p], nums[q]])
                    # update so there is no duplicates
                    p += 1
                    while p < q and nums[p] == nums[p - 1]:
                        p += 1

                    # update right pointer
                    q -= 1
                    while p < q and nums[q] == nums[q - 1]:
                        q -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
