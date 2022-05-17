# NOTE: this implementation FAILED due to exceeding time limit.
#
#  Saved for educational purposes.
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = 0

        for (day, purchase) in enumerate(prices):
            for sale in prices[day+1:]:
                profit = sale - purchase
                if profit > highest_profit:
                    highest_profit = profit

        return highest_profit
    