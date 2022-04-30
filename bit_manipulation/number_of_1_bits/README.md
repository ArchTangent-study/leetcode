# Number of 1 Bits ([LC191](https://leetcode.com/problems/number-of-1-bits/))
Difficulty: **Easy**

## Problem

Write a function that takes an unsigned integer `n` and returns the number of '1' bits it has (also known as the [Hamming weight](http://en.wikipedia.org/wiki/Hamming_weight)).

Constraints:
- The input must be a **binary string** of length `32`.

Follow up: If this function is called many times, how would you optimize it?

## Thought Process

Requirements:
- Input: an *unsigned* `int`, treated as a binary string (e.g. `00000000000000000000000000001011`).
- Output: an `int` representing the number of `1` bits in the input.

Edge Cases / Caveats:
- *unsigned* integers only.
- `0` always returns `0` bits.
- the number of bits in maximum *unsigned* integers may vary by language.

Approaches:

**Bit Shifting**: while `n` is greater than `0`:
- check if the least significant bit (LSB) is `1`.  If so, increment `count`.
- shift bits to the right.

Complexity:
- Time: `O(1)` (constant), as all integers are the same size (32-bits).
- Space: `O(1)`, as space does not scale with input (only a single integer, `count`)

## Procedure

### Method 1: Bit Shifting

Performed as desribed in *Thought Process* above.

A key idea is to use `n & 1` to isolate the least significant bit.

### Method 2: Follow-Up

*(To be continued)*

## Results (Python 3)

**Method 1**:  51 ms, 13.8 MB (30.55%, 95.25%)
