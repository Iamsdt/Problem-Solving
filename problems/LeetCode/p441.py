class Solution:
    # nive solution
    def arrangeCoins2(self, n: int) -> int:
        res = 0
        while n > res:
            res += 1
            n -= res

        return res

    # lets use binary search
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        res = 0
        while l <= r:
            mid = (l+r) // 2
            coins = (mid/2)*(mid+1)
            if coins > n:
                r = mid-1
            else:
                res = max(mid, res)
                l = mid+1

        return res


if __name__ == '__main__':
    print(Solution().arrangeCoins(5))