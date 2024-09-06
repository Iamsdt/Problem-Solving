from itertools import accumulate
from typing import List


class Solution:
    def minimumAverageDifference2(self, nums: List[int]) -> int:
        res = float('inf')
        index = -1
        for i in range(1, len(nums)+1):
            a = nums[:i]
            b = nums[i:]
            if not b:
                v = min(res, sum(a)//len(a))
                if v < res:
                    index = i-1
                    res = v
            else:
                value = abs((sum(a)//len(a))-(sum(b)//len(b)))
                if value < res:
                    index = i-1
                    res = value

        return index

    def minimumAverageDifference(self, nums: List[int]) -> int:
        total = len(nums)
        pref = list(accumulate(nums))
        
        ans = (pref[-1]//total, total-1)

        for i in range(total-1):
            a = pref[i]//(i+1)
            b = (pref[-1]- pref[i])//(total-i-1)
            diff = abs(a- b)

            ans = min(ans, (diff, i))

        return ans[1]




if __name__ ==  '__main__':
    print(Solution().minimumAverageDifference([2,5,3,9,5,3]))
    print(Solution().minimumAverageDifference([0]))