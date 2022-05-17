# NOTE: this implementation is accurate, but FAILED due to exceeding time limit.
#
#  Saved for educational purposes.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num_days = len(prices)
        # No profit if only one trading day
        if num_days == 1:
            return 0
        
        # At least two days are guaranteed
        highest_profit = 0
        buy_day = 0
        buy_day_limit = num_days - 1
        sell_day_limit = num_days
                        
        while buy_day < buy_day_limit:
            purchase = prices[buy_day]
            
            sell_day = buy_day + 1
            
            while sell_day < sell_day_limit:
                sale = prices[sell_day]
                
                # Shift buy day to sell day if a new lower price is found
                if sale < purchase:
                    # NOTE: -1 needed as buy_day incremented after break
                    buy_day = sell_day - 1
                    break
            
                profit = sale - purchase
                
                if profit > highest_profit:
                    highest_profit = profit
                
                sell_day += 1

            buy_day += 1 

        return highest_profit
        