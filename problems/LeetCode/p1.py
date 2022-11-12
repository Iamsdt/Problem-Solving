from typing import List


class Solution:

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        head = 0
        cu = 1
        
        while head < len(nums):
            if (nums[head]+nums[cu]) == target:
                return head, cu
            
            if cu == len(nums)-1:
                head += 1 
                cu = head + 1
            else:
                cu += 1

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
    print(sol.twoSum2([2,7,11,15], 9))