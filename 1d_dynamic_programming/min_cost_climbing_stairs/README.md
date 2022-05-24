# Min Cost Climbing Stairs ([LC746](https://leetcode.com/problems/min-cost-climbing-stairs/))
Difficulty: **Easy**

## Problem

You are given an integer array `cost` where `cost[i]` is the cost of `ith` step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `0`, or the step with index `1`.

Return *the minimum cost to reach the top of the floor*.

Constraints:
- `2 <= cost.length <= 1000`
- `0 <= cost[i] <= 999`

## Thought Process

Questions:
- What constitutes the "top" of the stairs (end condition)?

Edge Cases / Caveats / Pitfalls:
- `cost.length < 2`: N/A as per constraints
- `cost.length == 2`: just take `min(cost[0], cost[1])`
- skipping the last step:  "reaching the top" means reaching *past* the final index
- handling the choice of starting at first or second step:  you could run the same algorithm twice, and then compare.
- Same cost steps: if two choices have the same cost, choose the further one (as it's closer to the final step).
- OOB indexing
- zero-cost steps

## Visualization

The cost to step from any index `i` is equal to it's *own cost* plus the minimum of the costs at indexes `i-1` and `i-2`.
```
  i-2   i-1    i
-------------------
|  2  |  5  |  4  |     cost
-------------------
   0     1     2        index
```
The cost to step up from index `2` would be `4 + min(2, 5) = 6`.

Example 1: `cost = [0,1,2,2]`
```python
     0   1   2   3      index
     
     0   1   2   2      cost
    
   [ 0   1 ] 2   2      start: index 2
             ^
   [ 0   1 ] 2   2      add min(0, 1) to cost[2]
   
     0 [ 1   2 ] 2      move to index 3
                 ^
     0 [ 1   2 ] 3      add min(1, 2) to cost[3]
     
     0   1 [ 2   3 ]    move to index 4 (top)
                     ^
final_cost = min(cost[-1], cost[-2]) = min(2, 3) = 2

return 2
```

Example 2: `cost = [1,3,3,2]`
```python
     0   1   2   3      index
     
     1   3   3   2      cost
    
   [ 1   3 ] 3   2      start: index 2
             ^
   [ 1   3 ] 4   2      add min(1, 3) = 1 to cost[2]
   
     1 [ 3   4 ] 2      move to index 3
                 ^
     1 [ 3   4 ] 5      add min(3, 4) = 3 to cost[3]
     
     1   3 [ 4   5 ]    move to index 4 (top)
                     ^
final_cost = min(cost[-1], cost[-2]) = min(4, 5) = 4

return 4
```

## Procedure

### Method 1: Min Cost Moving Window

Use *dynamic programming* to get the minimum of the previous two steps (`i-1`, `i-2`), and add that minimum to the current step's cost.  Then, move to the next step and perform the same calculation.  

This *caches* (using *memoization*) the lowest previous step cost within each step, allowing the calculation to be done in a single pass.

Complexity:
- Time: `O(n)`
- Space: `O(1)`

## Results (Python 3)

**Method 1**: 62 ms, 14.1 MB (84.86%, 45.77%)
