from operator import index
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key = lambda x: x[0])
        
        res = [intervals[0]]

        for start, end in intervals[1:]:
            last = res[-1][1] 
            if start <= last:
                res[-1][1] = max(last, end)
            else:
                res.append[start, end]


        return res



print("Solution", Solution().merge([[1,4],[2,3]]))