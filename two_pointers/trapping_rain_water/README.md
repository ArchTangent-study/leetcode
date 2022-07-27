# Trapping Rain Water ([LC042](https://leetcode.com/problems/trapping-rain-water/))
Difficulty: **Hard**

## Problem

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

Constraints:
- `n == height.length`
- `1 <= n <= 2 * 10⁴`
- `0 <= height[i] <= 10⁵`

## Thought Process

Questions:
- How are the edges treated?  From the example, it seems that they trap no water.

Edge Cases / Caveats / Pitfalls:
- Completely flat terrain
- Water leaking off of left and right edges (not collected)

Ideas:
- Monotonic Stack
- Two Pointers

## Procedure

### Method 1: Monotonically-Decreasing Stack

Key Idea: a *monotonically-decreasing stack* keeps the *highest* value at the leftmost side (`0th` index).  This acts as the left of the effective container.

Pitfall: when an incoming `(ix, ht)` pair contributes to total rainfall, it takes the index of the `(ix, ht)` pair that was popped from the stack.

Complexity:
- Time: `O(n)`
- Space: `O(n)`

Thoughts:
- The low score in memory consumption implies that there's a way to get better space complexity (perhaps `O(1)`)

### Method 2: Two Pointer w/ Highest Left/Right Value

Key Idea: use *two passes* to calculate area using highest left/rightmost values for a given index.

Big Picture:
1. In the first pass, gather the highest *leftmost* value for a given index
2. In the second pass (reverse):
    - gather the highest *rightmost* value for the index
    - get `area` using *lowest* of leftmost/rightmost height relative to current `height`
    - add `area` to `answer`
3. Return `answer`

Complexity:
- Time: two passes -> `O(2n)` -> `O(n)`
- Space: `O(n)`

Thoughts:
- This was slower than Method 1, likely due to having to do two passes.

## Results (Python 3)

**Method 1**: 148 ms, 16.5 MB (79.40%, 6.31%)

**Method 2**: 215 ms, 16.1 MB (38.47%, 41.59%)
