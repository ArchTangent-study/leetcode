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

### Method 2: Double Iterator Version 2 (Timeout)

*Note*: this method *also* timed out, but is worth discussing.

After the failed brute force approach in method 1, what's a way to improve upon it?
- Think: "buy low, sell high"
- Early exit: end iteration when certain conditions are present:
    - `profit` is equal to max possible profit
    - `purchase` price is the maximum (can't possibly sell at a profit)
    - `purchase` price on a given day is higher than any previous day -- it's *impossible* to make more profit than on the earlier day
- Improve calculations: instead of calculating `profit` every time, only calculate if the `sale` price is greather than `purchase` price.

### Method 3: Shifting Iterator

The first two methods were on the right track, but weren't efficient enough.  The third time still failed.

Key Changes:
- For a given `buy_day` pointer, as soon as you find a `sell_day` pointer that is ***lower*** than the `buy_day` price, ***stop and shift*** the `buy_day` pointer to the `sell_day` pointer's position.  Once you've found a lower purchase price than the current one, there's no point in continuing to explore that price.
    - IOW, move the `buy_day` to the `sell_day` whenever the `sell_day`'s price is lower than that of the `buy_day`.

Time Complexity: `O(n²)`.  This may be what's causing the time limit to be exceeded.

### Method 4: Shifting Iterator (Refined)

The most succinct approach I could find.

Key Changes:
- Instead of starting with lefmost pointer (`buy_day`) and *pushing* the right pointer to the right, start with the rightmost pointer (`sell_day`) and *pull* the leftmost pointer to the right.

Time Complexity: `O(n)`, since we're traversing the array only once.

## Results (Python 3)

**Method 1**:  FAILED - Time Limit Exceeded

**Method 2**:  FAILED - Time Limit Exceeded

**Method 3**:  FAILED - Time Limit Exceeded

**Method 4**:  1666 ms, 24.9 MB (21.43%, 95.98%)

## Lessons Learned

1. Draw it out: in this particular case, draw examples as you would an actual stock chart.  It makes finding a solution much easier.
2. When using direct indexing (vice Python iterators which take care of that for you), always be sure that you're in bounds!
3. While brute force may provide a working solution, their performance may not be sufficient.
