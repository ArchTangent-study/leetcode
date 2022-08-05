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
- Bit operations with Python

## Procedure

### Method 1: Bitwise Addition & Subtraction

*Warning*: Python's behavior when using bitwise addition (`&`) caught me off-guard when using negative numbers.  `2 & 16 = 0`, but `-2 & 16 = 16` and `-2 & -16 = -16`.

*Note* this approach was fraught with edge cases and headaches.  Surely there's a better way!

Visualization
|   `A`   |   `B`  |  Answer                                                   |
|---------|--------|-----------------------------------------------------------|
|   `0`   |  any   | `B`                                                       |
|   any   |   `0`  | `A`                                                       |
|  `> 0`  |  `>0`  | `abs(A) + abs(B)`                                         |
|  `< 0`  |  `<0`  | `-(abs(A) + abs(B))`                                      |
|  `> 0`  |  `<0`  | `abs(A) + abs(B)` with sign based on `abs(A)` vs `abs(B)` |
|  `< 0`  |  `>0`  | `abs(A) + abs(B)` with sign based on `abs(A)` vs `abs(B)` |

Complexity:
- Time: add or subtract 10 bits max, plus carry (highest magnitude = 1,000) -> `O(1)`
- Space: `O(1)`

### Method 2: BiXOR Sum, BitAND Carry (Rust)

Turns out, there was a better way, but it's very hard to do in Python without some hassle.  So for this, I chose my second language, *Rust*, for the implementation.

Complexity:
- Time: `O(1)`
- Space: `O(1)`

## Results (Python 3)

**Method 1**:  44 ms, 14.0 MB (58.01%, 14.41%)

## Results (Rust)

**Method 2**:  1 ms, 2.3 MB (68.09%, 8.51%)
