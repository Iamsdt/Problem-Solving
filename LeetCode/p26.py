from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i<len(nums)-1:
            if nums[i] != nums[i+1]:
                i = i+1
            else:
                nums.remove(nums[i])
        return i+1



if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums))
    print(nums)


