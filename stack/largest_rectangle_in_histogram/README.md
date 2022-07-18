# Largest Rectangle in Histogram ([LC084](https://leetcode.com/problems/largest-rectangle-in-histogram/))
Difficulty: **Hard**

## Problem

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the *area of the largest rectangle in the histogram*.

Constraints:
- `1 <= heights.length <= 10⁵`
- `0 <= heights[i] <= 10⁴`

## Thought Process

Edge Cases / Caveats / Pitfalls:

Notes:
- A single bar can count toward the answer
- The *lowest* included bar is the most limiting
- area of any set of group of bars is `num_bars * ht_of_lowest_bar`
- brute force would check every possible combination of bars -> `O(n²)`

## Procedure

### Method 1

## Results (Python 3)

**Method 1**:   ms,  MB (%, %)
