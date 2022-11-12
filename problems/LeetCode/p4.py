from typing import List
import numpy as np


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # num = nums1 + nums2
        # a = sorted(num)
        # lstLen = len(a)
        # index = (lstLen - 1) // 2
   
        # if (lstLen % 2):
        #     return a[index]
        # else:
        #     return (a[index] + a[index + 1])/2.0

        # numpy solution
        return np.median(np.sort(np.append(nums1, nums2)))

    


print(Solution().findMedianSortedArrays([1, 2], [4, 3]))
