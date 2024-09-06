class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 1, num+1
        while l <= r:
            m = (l+r)//2
            v = m*m
            if v == num:
                return True
            
            if num < v:
                r = m -1
            elif num > v:
                l = m + 1

        return False

if __name__ == "__main__":
    print(Solution().isPerfectSquare(16))
    print(Solution().isPerfectSquare(14))
