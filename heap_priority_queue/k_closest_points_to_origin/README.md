# K Closest Points to Origin ([LC973](https://leetcode.com/problems/k-closest-points-to-origin/))
Difficulty: **Medium**

## Problem

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane and an integer `k`, return the `k` *closest points to the origin* `(0, 0)`.

The distance between two points on the **X-Y** plane is the Euclidean distance (i.e., `√(x1 - x2)² + (y1 - y2)²`).

You may return the answer in **any order**. The answer is **guaranteed** to be **unique** (except for the order that it is in).

Constraints:
- `1 <= k <= points.length <= 10⁴`
- `-10⁴ < xi, yi < 10⁴`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- efficient distance calculation

## Procedure

### Method 1: Min Heap with Absolute Distance

Big Picture:
1. Absolute distance is `x*x + y*y` ; no need for `sqrt()`
2. Store *min heap* of `[abs_dist, x, y]` triplets
3. Extract the top `k` `[x, y]` values from the `heap` and add to `answer`
4. Return `answer`

Complexity:
- Time: heap insertion for all `n` items in input -> `O(n log n)`
- Space: store up to `n` items from input in `heap` -> `O(n)`

## Results (Python 3)

**Method 1**: 1104 ms, 20.5 MB (64.41%, 38.27%)
