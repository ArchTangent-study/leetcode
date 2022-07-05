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
- Prices are in *descending* order (e.g. `[5,4,3,2,1]`) -> no profit
- Out of Bounds (OOB): direct indexing can lead to OOB errors

## Procedure

### Method 1: Iteration

Key Steps:
1. Start with `hi` and `lo` at day 0's `price`, with `profit` of `0`
2. Iterate over each `price` in `prices`
3. If new low (`price < lo`):  reset both `lo` and `hi` to new low
4. If new high (`price > hi`): update `profit` if higher than previous `profit`

Complexity:
- Time: `O(n)`

### Method 2: Shifting Iterator

Effectively a  Two Pointer method.

Key Idea: movesthe `buy_day` to the `sell_day` whenever the price at `sell_day` is lower than that on the `buy_day`.

Complexity:
- Time: `O(n)`

## Results (Python 3)

**Method 1**:  1623 ms, 25.0 MB (41.12%, 38.06%)

**Method 2**:  1666 ms, 24.9 MB (21.43%, 95.98%)

## Lessons Learned

1. Draw it out: in this particular case, draw examples as you would an actual stock chart.  It makes finding a solution much easier.
2. When using direct indexing (vice Python iterators which take care of that for you), always be sure that you're in bounds!
3. While brute force may provide a working solution, their performance may not be sufficient.
