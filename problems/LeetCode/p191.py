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
            print(n)
        
        return count


if __name__ ==  '__main__':
    print(Solution().hammingWeight(11111111111111111111111111111101))    

