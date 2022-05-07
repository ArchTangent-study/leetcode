# Missing Number ([LC268](https://leetcode.com/problems/missing-number/))
Difficulty: **Easy**

## Problem

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the *only number in the range that is missing from the array*.

Constraints:
- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- All the numbers of `nums` are **unique**.

Follow up: Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?

## Thought Process

Edge Cases / Caveats:
- `n = 1` (single value)
- missing value is `n`

## Procedure

### Method 1: Simple Iteration

A simple and intuitive solution, though highly inefficient.

Approach:
1. Set `n = len(nums)`
2. Go over every `i` in `n`
3. If `i` is not in `nums`, return `i`

### Method 2: Sorted List

This is **23x** faster than method 1.

Key Ideas:
- Sorting and uniqueness means that `nums[i] = nums[i-1] + 1` for all but the case of the missing number.
- `nums` is never empty (`nums` is at least `[0]`)

Approach:
1. Sort `nums` in place
2. Set `expected` to `0`, since first value in sorted list will be `0`
3. Iterate over each `n` in `nums`
    - if `n == expected`, increment `expected` by `1` and continue
    - if `n != expected`, return `expected`
4. If all `n` in `nums` are traversed without returning, return `expected`, the length of the list.

## Results (Python 3)

**Method 1**:  3762 ms, 15.2 MB (6.38%, 35.71%)

**Method 2**:  163 ms, 15.2 MB (65.94%, 78.83%)
