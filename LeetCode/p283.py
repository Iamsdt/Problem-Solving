from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m, n = 0, 1
        while m < len(nums) and n < len(nums):
            if nums[n] == 0 and nums[m] == 0:
                n += 1
                continue
            
            if not nums[m]:
                nums[m], nums[n] = nums[n], nums[m]

            n +=1
            m +=1
        
        return nums


if __name__ == '__main__':
    print(Solution().moveZeroes([0,1,0,3,12]))
    print(Solution().moveZeroes([0, 0, 2, 3, 0]))
    print(Solution().moveZeroes([0]))
    print(Solution().moveZeroes([1, 0, 1]))
