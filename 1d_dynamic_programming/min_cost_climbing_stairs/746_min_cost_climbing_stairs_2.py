from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Iterative approach w/o mutation."""
        # Base case - 2 is lowest length of `cost` per constraints
        if len(cost) == 2:
            return min(cost[0], cost[1])

        top = len(cost)
        one_back = cost[1]
        two_back = cost[0]
        # Start from step at index 2 and stop at last step (just before top)
        for step in range(2, top):
            # Cost at current step is cost[step] + lowest of previous two steps
            step_cost = cost[step] + min(one_back, two_back)
            # Reassign steps (advance each forward one step)
            two_back, one_back = one_back, step_cost

        # At the top - return lowest of last two steps
        return min(one_back, two_back)