# Largest Rectangle in Histogram ([LC084](https://leetcode.com/problems/largest-rectangle-in-histogram/))
Difficulty: **Hard**

## Problem

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the *area of the largest rectangle in the histogram*.

Constraints:
- `1 <= heights.length <= 10⁵`
- `0 <= heights[i] <= 10⁴`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Proper indexing
- Accounting for area to left and right of each bar

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

### Method 2: Two-Pass Strict Monotonically-Increasing Stack w/Count

Big Picture:
1. Count all `bars` >= current `bar` using a (strictly) monotonically-intcreasing stack:
    - to bar's left (`left_count`)
    - to bar's right (`left_count`)
2. Include itself to calculate area:
    - `area = (1 + left_count + right_count) * height`

Complexity:
- Time: two `count` passes, one `area` pass -> `O(3n)`-> `O(n)`
- Space: one `stack` and one `count` list -> `O(2n)` -> `O(n)`

## Results (Python 3)

**Method 1**:  1401 ms, 28.3 MB (59.75%, 63.70%)

**Method 2**:  1317 ms, 27.8 MB (66.99%, 85.15%)
