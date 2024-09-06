class Solution:
    def maxProduct(self, nums: int) -> int:
        res = max(nums)
        cu_min, cu_max = 1, 1

        for n in nums:
            if n == 0:
                cu_min, cu_max = 1, 1
                continue
            
            temp = n*cu_max
            cu_max = max(n*cu_max, n*cu_min, n) #some language doesn's allow [-1, 8]
            cu_min = min(temp, n*cu_min, n) # [-1, -8], we want -8
            res = max(res, cu_max)

        return res
