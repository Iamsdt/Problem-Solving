from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        res = []
        for i, v in enumerate(nums):
            if v in di:
                return [di[v], i]
            
            di[target - v] = i
                
        return res
            
            
if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))