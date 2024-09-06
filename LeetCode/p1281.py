class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        a = 0
        while n:
            v =  n - (n//10)*10
            p *= v
            a += v
            n //= 10
        
        return p-a
        