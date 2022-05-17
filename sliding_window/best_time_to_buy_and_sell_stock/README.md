# Best Time to Buy and Sell Stock ([LC121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/))
Difficulty: **Easy**

## Problem

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the *maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return 0``.

Constraints:
- `1 <= prices.length <= 10⁵`
- `0 <= prices[i] <= 10⁴`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Single price given -> no profit
- Prices are in ascending order -> no profit

## Procedure

### Method 1: Double Iterator (Timeout)

*Note*: this method timed out, but is worth discussing as it (1) provides the correct answer, and (2) can be improved upon.

Key Steps:
1. Store a `highest_profit` value defaulting to `0` (fallback).
2. Start with a `purchase` in the `ith` index of `prices`, and a `sale` in the `i + 1` index.
3. Calculate `profit` as `sale - purchase`
4. If `profit > highest_profit`, set `highest_profit` to `profit`
5. Iterate over remaining `sale` values in `prices` and repeat steps `3` and `4`.
6. Increment `purchase` and `sale` indexes by `1` and repeat from step `2`, until all `purchase` values have been calculated.
7. Return `highest_profit`

Time Complexity: `O(n²)`.  This may be what's causing the time limit to be exceeded.

## Results (Python 3)

**Method 1**:  FAILED - Time Limit Exceeded

**Method 2**:  ms,  MB (%, %)
