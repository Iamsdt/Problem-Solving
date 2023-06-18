from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = Counter(nums)
        print(di)   
        print(di.keys())
        return list(di.keys())[:k]
        
        
if __name__ ==  '__main__':
    print(Solution().topKFrequent(nums = [3,0,1,0], k = 2))