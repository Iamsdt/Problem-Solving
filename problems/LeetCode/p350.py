from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        di1 = Counter(nums1)
        di2 = Counter(nums2)
        res = []
        for i in di1.keys():
            if i in di2:
                v = min(di1[i], di2[i])
                res.extend([i]*v)
        
        return res




if __name__ == '__main__':
    sol = Solution()
    print(sol.intersect([1, 2, 2, 1], [2, 2]))