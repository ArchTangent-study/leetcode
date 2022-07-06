from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo, hi, profit = prices[0], prices[0], 0
        
        for price in prices:
            # If new low, reset current low and high
            if price < lo:
                lo = price
                hi = price
            # if new high, update profit
            if price > hi:
                hi = price
                profit = max(profit, hi - lo)
            
        return profit
        