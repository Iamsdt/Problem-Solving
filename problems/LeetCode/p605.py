import re
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        li = [0]+flowerbed+[0]
        for i in range(1, len(li)-1):
            if li[i-1] == 0 and li[i] ==0 and li[i+1] ==0:
                li[i] = 1
                n -= 1

        return n <= 0

    
# solution 2
class Solution2:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = 0 if flowerbed[0] else 1
        for f in flowerbed:
            if f:
                n -= int((empty-1)/2)
                empty = 0
            else:
                empty += 1
            
        n -= empty//2
        return n <= 0


        
if __name__ == '__main__':
    print(Solution2().canPlaceFlowers([0, 0, 1, 0, 1], 2))
    print(Solution2().canPlaceFlowers([1,0,0,0,1], 1))
    print(Solution2().canPlaceFlowers([1,0,0,0,1], 2))
    print(Solution2().canPlaceFlowers([1,0,0,0,1,0,0], 2))