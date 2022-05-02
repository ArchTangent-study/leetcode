# Counting Bits ([LC338](https://leetcode.com/problems/counting-bits/))
Difficulty: **Easy**

## Problem

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i (0 <= i <= n)`, `ans[i]` is the **number** of `1`s in the binary representation of `i`.

Constraints:
- `0 <= n <= 10^5`

Follow up:
- It is very easy to come up with a solution with a runtime of `O(n log n)`. Can you do it in linear time `O(n)` and possibly in a **single pass**?
- Can you do it without using any built-in function (i.e., like `__builtin_popcount` in C++)?

## Thought Process

Requirements:
- input `n` is an integer
- `ans` has a length of `n + 1`
- for each `i` in `n`, `ans[i]` is number of `1`s in bitwise representation of `i`

Edge Cases / Caveats:
- `n >= 0`
- `ans[0]` is always `0`

Approach 1: Iterative Bit Shifting (see below)

## Visualization

There's a clear pattern when looking at the bitwise representation of `0` to `16`:
```
00000   0
00001   1
00010   2
00011   3
00100   4
00101   5
00110   6
00111   7
01000   8
01001   9
01010   10
01011   11
01100   12
01101   13
01110   14
01111   15
10000   16
```

## Procedure

### Method 1: Iterative Bit Shifting

This builds upon the techniques applied in the **Number of 1 Bits** [LC191](https://github.com/ArchTangent-study/leetcode/tree/main/bit_manipulation/number_of_1_bits) problem.

This is effectively the same problem, but done for a range of numbers instead of a single one.

Time complexity: `O(n log(n))`

## Results (Python 3)

**Method 1**:  198 ms, 20.7 MB (23.22%, 80.59%)
