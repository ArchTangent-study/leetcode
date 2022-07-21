# Two Sum II - Input Array is Sorted ([LC167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/))
Difficulty: **Medium**

## Problem

Given a **1-indexed** array of integers `numbers` that is already ***sorted in non-decreasing order***, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1₁` and `numbers[index₂]` where `1 <= index₁ < index₂ <= numbers.length`.

Return the indices of the two numbers, `index₁` and `index₂`, ***added by one*** as an *integer array* `[index₁, index₂]` of *length 2*.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant (`O(1)`) extra space.

Constraints:
- `2 <= numbers.length <= 3 * 10⁴`
- `-1000 <= numbers[i] <= 1000`
- numbers is sorted in **non-decreasing order**.
- `-1000 <= target <= 1000`
- The tests are generated such that there is **exactly one solution**.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Proper indexing (`1`-indexed)
- Constant space `O(1)`
- Only one answer
- Can only use each element once
- Multiples of same value, e.g. `[1,2,2,2,3]`

Ideas:
- Since values are non-decreasing, early exit can be used once a value higher than `target` is found.

## Procedure

### Method 1: Two Pointers Naive w/Early Exit

Key Idea: a naive (brute force) two pointers approach with early exit if the `combined` sum is greater than `target`.

Complexity:
- Time: `O(n²)`
- Space: `O(1)`

## Results (Python 3)

**Method 1**:  ms, MB (%, %)
