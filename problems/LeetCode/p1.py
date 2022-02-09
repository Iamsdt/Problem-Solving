from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i, v in enumerate(nums):
            r = target - v
            if r in di:
                return [di[r], i]
            else:
                di[v]=i


        return [0, 0]



if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))