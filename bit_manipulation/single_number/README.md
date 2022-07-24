# Single Number ([LC136](https://leetcode.com/problems/single-number/))
Difficulty: **Easy**

## Problem

Given a **non-empty** array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity (`O(n)`) and use only constant extra space (`O(1)`).

Constraints:
- `1 <= nums.length <= 3 * 10^4`
- `-3 * 104 <= nums[i] <= 3 * 10^4`
- Each element in the array appears twice except for one element which appears only once.

## Procedure

### Method 1: Bit Exclusive Or (XOR)

1. Start with a `value` of `0`.
2. For each `number` in `nums`:
    - set `value = value ^ number`
3. Return `value`

The principles:
- `0 ^ number = number`: any number bitwise XORed with `0` is itself.
- `number ^ number = 0`: any number bitwise XORed with itself is `0`.

Thus, any duplicates will negate themselves, and the only unpaired value in `nums` will be the answer.

Complexity:
- Time: `O(n)`
- Space: `O(1)`

## Results (Python 3)

**Method 1**:  196 ms, 16.8 MB (45.03%, 52.85%)

### Alternatives

The first method I considered involved *sorting*: sort the list and then compare each pair of objects numbers to each other.

Runtime complexity is `O(nlogn)` due to the sorting, so it doesn't meet the time complexity requirement of `O(n)`.
