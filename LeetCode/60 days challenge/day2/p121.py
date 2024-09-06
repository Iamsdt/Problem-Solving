from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in prices:
            for jj in range(i+1, len(prices)):
                tp = prices[jj] - i
                profit = max(tp, profit)

        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        invest = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < invest:
                invest = prices[i]
            else:
                profit = max(prices[i]-invest, profit)

        return profit


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
