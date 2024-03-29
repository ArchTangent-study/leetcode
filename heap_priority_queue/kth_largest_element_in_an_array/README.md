# Kth Largest Element in an Array ([LC215](https://leetcode.com/problems/kth-largest-element-in-an-array/))
Difficulty: **Medium**

## Problem

Given an integer array `nums` and an integer `k`, return the `kth` *largest element in the array*.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Constraints:
- `1 <= k <= nums.length <= 10⁴`
- `-10⁴ <= nums[i] <= 10⁴`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Duplicate numbers (don't need `kth` largest *distinct* element)
- Time complexity constraint of `O(n)`

Approaches:
- Min Heap: will fail due to `O(n log n)` complexity being above requirements

Thoughts:
- Considering how slow both accepted methods were, perhaps there's a better way?

## Procedure

### Method 1: List Counter

Key Idea: take advantage of limited number range (`-10000 to +10000`) to count each number in a single list.  Then, counting down from the highest number, lowering `k_remaining` until you get to the `kth` highest element.

Complexity:
- Time: `O(n)`
- Space: `O(1)`

### Method 2: Quickselect

Key Idea: the worst case time complexity is `O(n²)`, but this can be mitigated by choosing a random pivot in the middle (e.g. `len(numbers) // 2`).

Complexity:
- Time: `O(n²)`, but `O(n)` average case with middle-index pivot (rather zero index)
- Space: `O(n)`

### Failed Method: Monotonically-Decreasing Stack using Deque of Length K

This works fine in the average case, but the worst case time complexity of `O(n²)` causes this to fail on TLE.

Complexity:
- Time: `O(n²/8)` -> `O(n²)`
- Space: `O(n²)`

## Results (Python 3)

**Method 1**: 952 ms, 24.5 MB (17.99%, 21.58%)

**Method 2**: 699 ms, 27.4 MB (25.32%, 9.09%)
