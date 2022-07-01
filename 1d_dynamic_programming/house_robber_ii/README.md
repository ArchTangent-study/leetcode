# House Robber II ([LC213](https://leetcode.com/problems/house-robber-ii/))
Difficulty: **Medium**

## Problem
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle**. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array nums representing the amount of money of each house, return *the maximum amount of money you can rob tonight* ***without alerting the police***.

Constraints:
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

## Thought Process

Questions:
- is a single house adjacent to itself?

Edge Cases / Caveats / Pitfalls:
- Looping: making multiple passes (since houses are in a circle)

## Procedure

### Method 1: Two-Pass Iterative DP

Visualization:
```
nums = [4,1,3,1,5]

     v
    [4,1,3,1,_]     1st pass: exclude last house -> do not iterate over it
       v
    [4,1,3,1,_]
         v
    [4,1,3,1,_]
           v
    [4,1,3,1,_]

    Keep 4 and 3 -> result of 1st pass: 7

       v
    [0,1,3,1,5]     2nd pass: exclude 1st house -> treat it as zero; start at index 1
         v
    [0,1,3,1,5]
           v
    [0,1,3,1,5]
             v
    [0,1,3,1,5]

    Keep 5 and 3 -> result of 2nd pass: 8

    Answer: highest of 1st/2nd passses -> max(7,8) = 8
```

Key Idea: you can't visit the first house (index `[0]`) and the last house (index `[1]`) in the same pass -> they are *mutually exclusive*.  You can, however, test two *separate passes*, one where the first house is excluded, and one where the last house is excluded.  This precludes the chance of both being robbed in the same run.

Big Picture: similar to that of House Robber ([LC198](https://leetcode.com/problems/house-robber/))
1. Perform two passes, according to rules below.
2. If only one house, rob that house
3. If two houses, rob the one with more money
4. If three or more houses, gather highest running total using a moving window, from `index [0]` to `index [last-1]` for 1st pass and `index [1]` to `index [last]` for 2nd pass.
5. Highest value at any house is the highest of:
    - current house + three houses back
    - current house + two houses back
    - one house back
6. Update the highest value and advance the three-house window forward
7. Return the highest result of the two passes

Complexity:
- Time: two passes through `n` values -> `O(2n)` -> `O(n)`
- Space: constant number of space regardless of `n` -> `O(1)`

## Results (Python 3)

**Method 1**: 33 ms, 13.9 MB (**91.72%**, 71.04%)
