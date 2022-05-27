# Maximum Subarray ([LC053](https://leetcode.com/problems/maximum-subarray/))
Difficulty: **Easy**

## Problem

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return *its sum*.

A **subarray** is a **contiguous** part of an array.

Constraints:
- `1 <= nums.length <= 10⁵`
- `-10⁴ <= nums[i] <= 10⁴`

Follow up: If you have figured out the `O(n)` solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Empty array (N/A as per constraints)
- Negative numbers (can still be negative and be the highest)
- Zero values in `nums` (higher than any negative)

Approaches:
1. Brute force: attempt every possible contiguous subarray -> `O(n³)`
2. Iterate forward, taking a running sum of all values, then iterate backward, collecting the largest sum from the highest point.

## Procedure

### Method 1: Dynamic Programming

Key Ideas:
- Any negative `running_sum`s that come before current number in `nums` can be discarded.

Key Steps:
1. Store `running_sum` and `highest_sum` values.
    - *Note*: `highest_sum` should be initialized to the *lowest possible integer*
2. Iterate over each `num` in `nums`
3. Set `running_sum` to `max(num, running_sum + num)`.
    - So if `running_sum < 0`, `running_sum = num`.  That is, ignore any *negative* values to the left of the current number.
4. If `running_sum` is higher than `highest_sum`, replace `highest_sum` with that value.
5. Return `highest_sum` at the end of the iteration.

Complexity:
- Time: done in a single pass -> `O(n)`
- Space: two integer variables -> `O(1)`

Pitfalls:
- Initializing default `highest_sum` value to `0` instead of minimum integer

## Results (Python 3)

**Method 1**:  ms, MB (%, %)

## Lessons Learned
1. If stuck, start with simplest approach you can think of, then build on it
2. The lowest number in Python can be expressed as `-sys.maxsize - 1`
