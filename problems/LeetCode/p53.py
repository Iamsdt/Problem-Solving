from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_res = nums[0]
        
        current = 0
        
        for i in nums:
            if current < 0:
                print("Reset", i)
                current = 0
                
            current += i
            max_res =  max(max_res, current)    
            print("current", i, current, max_res)
            
            
        return max_res



if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))