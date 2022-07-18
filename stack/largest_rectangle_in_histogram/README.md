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

## Key Ideas
The area for any given bar in the histogram is based on `count * height`, where `count` is:
1. itself (`1`), plus
2. number of *contiguous* rectangles of *same or greater* height to bar's left, plus
3. number of *contiguous* rectangles of *same or greater* height to bar's right

And `height` is the `height` of the `bar`.  The equation for any `bar` in `heights`:
```python
area = (1 + num_contiguous_bars_left + num_contiguous_bars_right) * height
```

Other Key ideas:
1. The last item left in a monotonically-increasing stack (at end of iteration) is the *lowest* value in the entire set of values.  When calculating its area, it should extend *fully* to the left *and* right of the list (to `0` and `len(heights) - 1`)

## Procedure

### Method 1: Monotonically-Increasing Stack

Complexity:
- Time: `O(n)`
- Space: `O(n)`

## Results (Python 3)

**Method 1**:  1401 ms, 28.3 MB (59.75%, 63.70%)
