from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        invest = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < invest:
                invest = prices[i]
            else:
                profit = max(prices[i] - invest, profit)

        return profit



if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([2,4,1]))