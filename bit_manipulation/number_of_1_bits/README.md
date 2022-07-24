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

Approach 1: Bit Shifting

While `n` is greater than `0`:
- check if the least significant bit (LSB) is `1`.  If so, increment `count`.
- shift bits to the right.

Complexity:
- Time: `O(1)` (constant), as all integers are the same size (32-bits).
- Space: `O(1)`, as space does not scale with input (only a single integer, `count`)

## Procedure

### Method 1: Bit Shifting

Performed as desribed in *Thought Process* above.

A key idea is to use `n & 1` to isolate the least significant bit.

Complexity:
- Time: shift up to `b` total bits in number -> `O(b)`
- Space:  constant extra space -> `O(1)`

### Method 2: Follow-Up

This method can be much faster for larger numbers, where the `1` bits are distributed toward the most significant bit (MSB), e.g. `1100000` vice `00000011`.

Instead of shifting bits in `n`, multiply `n` by `n-1`.  It's easier to just show what's happening - here's an example with an 8-bit integer:

```
n: u8 = 0b10000001

Step 1
10000001    n
10000000    n-1
10000000    n & (n-1)
       1    count

Step 2
10000000    n
01111111    n-1
00000000    n & (n-1)n&(n-1)
       2    count

Since n is now 0, return count, which is 2
```

In the above case, only two passes are required instead of 8.

Complexity:
- Time: shift up to `b` set bits -> `O(b)`
- Space:  constant extra space -> `O(1)`

## Results (Python 3)

**Method 1**:  51 ms, 13.8 MB (30.55%, 95.25%)

## Lessons Learned

In Python, it can be slightly faster to use `n &= n-1` than to use `n = n & (n-1)`.
