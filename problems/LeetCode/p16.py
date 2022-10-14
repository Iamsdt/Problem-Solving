from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums, res, n =sorted(nums), float("inf"), len(nums)
        
        for i in range(n-2):
            
            if i and nums[i] == nums[i-1]: #remove duplicate
                continue
            
            hi = n - 1
            
            lo = i+1
            
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if sum == target:
                    return target

                if abs(target-sum) < abs(target-res):
                    res = sum
                
                if sum < target:
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo+1]: #remove duplicate
                        lo += 1
                else:
                    hi -= 1
                    while lo < hi and nums[hi] == nums[hi-1]: #remove duplicate
                        lo += 1
                
        return res


if __name__ == "__main__":
    print(Solution().threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))