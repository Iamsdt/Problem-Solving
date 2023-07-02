from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = float("-inf")
        sell = 0
        for i in prices:
            buy = max(buy, sell - i)
            sell = sell = max(sell, buy + i - fee)

        return sell
