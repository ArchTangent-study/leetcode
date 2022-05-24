from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Cost at each step is minimum of (step-1, step-2)        
        final_step = len(cost)
        
        current_ix = 2
        
        while current_ix < final_step:
            # Compare one/two steps up and choose lower
            one_back = current_ix - 1
            two_back = current_ix - 2    
                
            # Update cost of current step by min of previous two steps
            lowest_cost = min(cost[one_back], cost[two_back])
                
            cost[current_ix] += lowest_cost

            current_ix += 1
        
        # At the top - return lowest of last two steps
        return min(cost[-1], cost[-2])
