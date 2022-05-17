# NOTE: this implementation is accurate, but FAILED due to exceeding time limit.
#
#  Saved for educational purposes.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = 0
        lowest_purchase = 10000 # Max value as per constraints
        highest_possible_profit = max(prices) - min(prices) # Not guaranteed to occur

        for (day, purchase) in enumerate(prices):
            # No need to check if today's price is higher than lowest seen so far
            if purchase > lowest_purchase:
                continue
            else:
                lowest_purchase = purchase
            for sale in prices[day+1:]:
                if sale < purchase:
                    continue

                profit = sale - purchase

                if profit > highest_profit:
                    # Early exit: highest profit found 
                    if profit == highest_possible_profit:
                        return profit
                    highest_profit = profit     

        return highest_profit
    