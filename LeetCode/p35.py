from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s,e = 0, len(nums)-1

        while s <= e:
            m = (s+e)//2
            # if s == e:
            #     return s+1 if nums[s] < target else s
            if nums[m] < target:
                s = m+1
            elif nums[m] > target:
                e = m-1
            elif nums[m] == target:
                return m

        return s


if __name__ == "__main__":
    print(Solution().searchInsert([1,3,5,6], 5))
    print(Solution().searchInsert([1,3,5,6], 2))
    print(Solution().searchInsert([1,3,5,6], 4))
    print(Solution().searchInsert([1,3,5,6], 7))
    print(Solution().searchInsert([1,3,5,6], 0))