from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        res = [0]* len(nums)
        insert = len(nums)-1
        while l <= r or insert >= 0:
            if abs(nums[l]) < abs(nums[r]):
                res[insert] = abs(nums[r])**2
                insert -= 1
                r -= 1
            else:
                res[insert] = abs(nums[l])**2
                insert -= 1
                l += 1

        return res


if __name__ == "__main__":
    print(Solution().sortedSquares([-4,-1,0,3,10]))
    print(Solution().sortedSquares([-7,-3,2,3,11]))
    
