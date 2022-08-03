# Sum of Two Integers ([LC371](https://leetcode.com/problems/sum-of-two-integers/))
Difficulty: **Medium**

## Problem

Given two integers `a` and `b`, return the **sum of the two integers** without using the operators `+` and `-`.

Constraints:
- `-1000 <= a, b <= 1000`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Negative numbers (subtraction)
- Carry on final bit checked
- Sign

## Procedure

### Method 1: Bitwise Addition & Subtraction

*Warning*: Python's behavior when using bitwise addition (`&`) caught me off-guard when using negative numbers.  `2 & 16 = 0`, but `-2 & 16 = 16` and `-2 & -16 = -16`.

*Note* this approach was fraught with edge cases and headaches.  Surely there's a better way!

## Results (Python 3)

**Method 1**:  44 ms, 14.0 MB (58.01%, 14.41%)
