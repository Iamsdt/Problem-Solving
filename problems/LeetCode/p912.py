from typing import List


class Solution:
    def sort(self, a:List[int], b:List[int])-> List[int]:
        res = []
        p, q = 0, 0
        
        while p < len(a) and q < len(b):
            if a[p] < b[q]:
                res.append(a[p])
                p += 1
            else:
                res.append(b[q])
                q += 1
                
        # now check anything left
        if p < len(a):
            res += a[p:]
        
        if q < len(b):
            res += b[q:]
        
        return res
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        # divide and conquer
        mid = len(nums) // 2
        a = self.sortArray(nums[:mid])
        b = self.sortArray(nums[mid:])
        return self.sort(a, b)