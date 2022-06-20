class Solution:
    def hammingWeight2(self, n: int) -> int:
        count = 0
        while n:
            count += n % 2
            n = n >> 1
        
        return count

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n % 2
            n = n >> 1
        
        return count

    

