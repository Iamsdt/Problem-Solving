from typing import List


class Solution:
    # useless tricky solution
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)).difference(set(nums)))

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n)-1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res

    


if __name__ == '__main__':
    print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))