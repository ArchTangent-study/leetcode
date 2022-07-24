# Container with Most Water ([LC011](https://leetcode.com/problems/container-with-most-water/))
Difficulty: **Medium**

## Problem

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the *maximum amount of water a container can store*.

**Note**: you may not slant the container.

Constraints:
- `n == height.length`
- `2 <= n <= 10⁵`
- `0 <= height[i] <= 10⁴`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Account for both directions
- Proper area calculation

Ideas:
- Monotonic stack?  Won't work
- Two Pointers

## Procedure

### Method 1

### Failed Method: Two Pointer Closing Window w/Early Exit

*Note*: this got correct results on all my testing but failed on "Time Limit Exceeded" for input `[*range(10001)] + [*range(10000, -1, -1)]` (a triangular distribution)

Complexity:
- Time: `O(n²)`
- Space: `O(1)`

## Results (Python 3)

**Method 1**:  ms, MB (%, %)
