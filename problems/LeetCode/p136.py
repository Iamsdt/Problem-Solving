

from collections import Counter
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = Counter(nums)
                
        for i in dic.keys():
            print(i, dic[i] == 1)
            if dic[i] == 1:
                return i
        
        return 0



if __name__ == '__main__':
    print(Solution().singleNumber([4,1,2,1,2]))