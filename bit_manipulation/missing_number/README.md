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

## Procedure

### Method 1: Simple Iteration

Approach:
1. Set `n = len(nums)`
2. Go over every `i` in `n`
3. If `i` is not in `nums`, return `i`

## Results (Python 3)

**Method 1**:  3762 ms, 15.2 MB (6.38%, 35.71%)
