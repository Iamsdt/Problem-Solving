class Solution:
    def threeSum(self, nums): 
        nums, res, n =sorted(nums), [], len(nums)
        
        for i in range(n-2):
            
            if nums[i] > 0: #pruning
                break
            
            if i and nums[i] == nums[i-1]: #remove duplicate
                continue
            
            hi = n - 1
            
            lo = bisect.bisect_left(nums, - nums[i] - nums[hi], i + 1, hi) - 1 #binary search
            
            lo += (lo == i)
            
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
            
                if sum == 0:
                    res += (nums[i], nums[lo], nums[hi]),
                    while lo < hi and nums[lo] == nums[lo+1]: #remove duplicate
                        lo += 1 
                    while lo < hi and nums[hi] == nums[hi-1]: #remove duplicate
                        hi -= 1
                        
                lo += sum <= 0 
                hi -= sum >= 0
                
        return res