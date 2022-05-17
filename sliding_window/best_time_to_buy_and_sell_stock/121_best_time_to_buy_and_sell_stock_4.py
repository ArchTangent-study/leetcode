from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = 0               
        buy_day = 0

        for sell_day in range(1, len(prices)):
            if prices[sell_day] < prices[buy_day]:
                buy_day = sell_day

            highest_profit = max(highest_profit, prices[sell_day] - prices[buy_day])

        return highest_profit
        