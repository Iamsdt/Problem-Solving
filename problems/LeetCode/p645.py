from typing import List
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        di = Counter(nums)
        ans = [0,0]
        for i in range(1,len(nums)+1):
            if di[i]==2:
                ans[0]=i
            if di [i]==0:
                ans[1]=i
        return ans

if __name__ ==  '__main__':
    print(Solution().findErrorNums([1,2,2,4]))
    print(Solution().findErrorNums([1,1]))
    print(Solution().findErrorNums([2,2]))
