# Binary Search ([LC704](https://leetcode.com/problems/binary-search/))
Difficulty: **Easy**

## Problem

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

Constraints:
- `1 <= nums.length <= 10⁴`
- `-10⁴ < nums[i], target < 10⁴`
- All the integers in `nums` are **unique**.
- `nums` is sorted in ascending order.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Empty list (impossible as per constraints)
- Single value (e.g. `[3]` or `[-5]`)
- `nums` not sorted (impossible as per constraints)
- multiple correct answers (more than 1 value in `nums` equals `target` (impossible as per constraints)
- Out of bounds (OOB) indexing

## Procedure

### Method 1: Binary Search

Apply an approach similar to "half-splitting" in electronics troubleshooting.  Repeatedly split the problem into two parts until you have found the answer or can't split any further.

Algorithm:
1. Create `left` and `right` index values at the lowest and highest index in `nums`, respectively.
2. Set `mid` index as the halfway point between `left` and `right` (`(left + right) // 2`).
3. Get the `guess` value at the `mid` index in `nums`.
4. If `guess` equals `target`, return the `mid` index as the answer.
5. if `guess` is less than `target`, `target` is "to the right" of `guess`
    - shift `left` index to `mid + 1` (since `mid` was already checked for the guess)
6. if `guess` is greater than `target`, `target` is "to the left" of `guess`
    - shift `right` index to `mid - 1` (since `mid` was already checked for the guess)
7. Repeat steps `3` to `6` while `left` is less than `right`.
8. If `left == right`, get *final* `guess` at `nums[left]`.
    - if `guess` equals `target`, return `left` index as the answer.
    - otherwise, `target` is not found -> return `-1`

Pitfalls:
- Order of operations: when calculating the middle (guess) index be sure to obey order of operations:
```python
mid_ix = left_ix + right_ix // 2    # WRONG
mid_ix = (left_ix + right_ix) // 2  # CORRECT
```

## Results (Python 3)

**Method 1**: 253 ms, 15.5 MB (82.50 %, 73.34%)
