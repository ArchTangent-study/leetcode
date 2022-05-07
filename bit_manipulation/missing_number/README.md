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

This is **~23x** faster than method 1.

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

### Method 3: Arithmetic Series

This is **~20x** faster than method 1.

Key Ideas:
- The [arithmetic series](https://en.wikipedia.org/wiki/Arithmetic_progression) can be used for a simple and fast solution
- Since there's only one missing value and all values are unique, the missing number is simply the sum of the arithmetic series from `1-n`, minus the sum of the numbers in `nums`.

Approach:
1. Set `n` to length of `nums`
2. Calculate sum of arithmetic series from `[1..n]`: `arithmetic_sum`
3. Calculate sum of values in `nums`: `sum_of_list`
4. Return `arithmetic_sum` - `sum_of_list`

### Method 4: Bitwise XOR Deduplication

This is **~26x** faster than method 1.

Key Idea: use bitwise XOR, also used in my Single Number ([LC136](https://github.com/ArchTangent-study/leetcode/tree/main/bit_manipulation/single_number)) solutions. Two rules:
- `0 ^ n = n`
- `n ^ n = 0`

Approach:
1. Set `answer` to `0`
2. For every `n` in `nums`: `answer ^= n`
3. For every `n` from `0` to `len(nums) + 1`: `answer ^= n`
4. Return `answer`

## Results (Python 3)

**Method 1**:  3762 ms, 15.2 MB (6.38%, 35.71%)

**Method 2**:  163 ms, 15.2 MB (65.94%, 78.83%)

**Method 3**:  185 ms, 15.1 MB (53.28%, 78.83%)

**Method 4**:  142 ms, 15.1 MB (83.19%, 78.83%)
