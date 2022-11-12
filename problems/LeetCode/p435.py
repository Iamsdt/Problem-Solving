from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) <= 1:
            return 0

        intervals.sort(key = lambda x: x[0])
        
        res = [intervals[0]]
        count = 0

        for start, end in intervals[1:]:
            last = res[-1][1] 
            if start < last:
                res[-1][1] = min(last, end)
                count += 1
            else:
                res.append([start, end])

        return count


print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]))