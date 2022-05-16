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
  2-3 vs 0-1             4-7 vs 0-3              8-15 vs 0-7
 bits    n  ct          bits    n  ct           bits    n  ct
0000 0   0   0          000 00   0   0          00 000   0   0
0000 1   1   1          000 01   1   1          00 001   1   1
                        000 10   2   1          00 010   2   1
0001 0   2   1          000 11   3   2          00 011   3   2
0001 1   3   2                                  00 100   4   1
                        001 00   4   1          00 101   5   2
                        001 01   5   2          00 110   6   2
                        001 10   6   2          00 111   7   3
                        001 11   7   3          
                                                01 000   8   1 
                                                01 001   9   2
                                                01 010  10   2
                                                01 011  11   3
                                                01 100  12   2
                                                01 101  13   3
                                                01 110  14   3
                                                01 111  15   4
```
For `2-3` vs `0-1`:
- The representation of `2` is the same as that of `0`, with a `1` at bit index `1`
- The representation of `3` is the same as that of `1`, with a `1` at bit index `1`

For `4-7` vs `0-3`:
- The representation of `4` is the same as that of `0`, with a `1` at bit index `2`
- The representation of `5` is the same as that of `1`, with a `1` at bit index `2`
- The representation of `6` is the same as that of `2`, with a `1` at bit index `2`
- The representation of `7` is the same as that of `3`, with a `1` at bit index `2`

For `8-15` vs `0-7`:
- The representation of `8` is the same as that of `0`, with a `1` at bit index `3`
- The representation of `9` is the same as that of `1`, with a `1` at bit index `3`
- The representation of `10` is the same as that of `2`, with a `1` at bit index `3`
- The representation of `11` is the same as that of `3`, with a `1` at bit index `3`

... and so on.

## Procedure

### Method 1: Iterative Bit Shifting

This builds upon the techniques applied in the **Number of 1 Bits** [LC191](https://github.com/ArchTangent-study/leetcode/tree/main/bit_manipulation/number_of_1_bits) problem.

This is effectively the same problem, but done for a range of numbers instead of a single one.

Time complexity: `O(n log(n))`

### Method 2: Dynamic Programming Version 1 (Follow-Up)

Using the pattern in the [Visualization](#visualization) section above:

- The results for `4-7` can *reuse* the results of `0-3`, adding `1` to the final count.
- The results for `8-15` can *reuse* the results of `0-7`, adding `1` to the final count.
- The results for `16-31` can *reuse* the results of `0-15`, adding `1` to the final count.
... and so on.

This can be turned into an algorithm:
1. Calculate `bit_count` for `i = [0..3]` using [Method 1](#method-1-iterative-bit-shifting).
2. For `i = [4..7]`, `bit_count[i]` == `bit_count[i-4]` (shift 4 indexes back, add `1`).
3. For `i = [8..15]`, `bit_count[i]` == `bit_count[i-8]` (shift 8 indexes back, add `1`).
4. For `i = [16..31]`, `bit_count[i]` == `bit_count[i-16]` (shift 16 indexes back, add `1`).

Time complexity: `O(n)`

**Thoughts**: This solution is clearly not ideal, as there's a pattern (*base 2*) that can be used to coalesce the many `for` loops in the solution into a single one.  See **method 3** for a better way.

### Method 3: Dynamic Programming Version 2 (Follow-Up)

Another look at the pattern:
- for `n = [1..1]`, the count for `n` is `1 + answer[n-1]`
- for `n = [2..3]`, the count for `n` is `1 + answer[n-2]`
- for `n = [4..7]`, the count for `n` is `1 + answer[n-4]`
- for `n = [8..15]`, the count for `n` is `1 + answer[n-8]`
- for `n = [16..31]`, the count for `n` is `1 + answer[n-16]`

... and so on.

Key idea: for every number `n`, there exists:
- a `count_index` equal to n (the index in the `count` return value)
- a `index_shift` equal to 2 * log2(n)
- a `bit_count` equal to `answer[n - index_shift] + 1`

The simplest way I found to determine the `index_shift` is to set it to a baseline level of `1`, and if `n > index_shift`, then double `index_shift`.

Example where `n = 5`:

```python
nums   = [0, 1, 2, 3, 4]    # numbers n tracked so far, from 0 to 4
answer = [0, 1, 1, 2, 1]    # count of bits for each n so far, from 0 to 4

index_shift = 2*log2(5) = 4

So, when n = 5:
    count_5 = answer[5 - 4] + 1
            = answer[1] + 1
            = 1 + 1
            = 2

nums   = [0, 1, 2, 3, 4, 5] 
answer = [0, 1, 1, 2, 1, 2] <- add count of 2 to the answer
```
Other notes:
- Since `n` is known in advance, you can preallocate the `answer` array to `[0]*n`
- For any value of `n`, the count for `n` is stored in `answer[n]`

Thoughts: this was about **40% faster** than method 2, while being more concise.

### Method 4: Dynamic Programming Refined

An attempt to make the above approaches more succinct and easier to understand.

Big Picture:
- Since `n` is known in advance, you can preallocate the `answer` array to `[0]*n`
- The bit count for each `number` in `n` is stored in an index equal to `number`.
- Each `number`'s bit count is equal to that of `number >> 1`, plus the **sign bit**.
- Sign bit can be calculated by taking `number % 2`

Example where `n == 5`:
1. `number = 0`: answer equals that of `0` (`0 >> 1 = 0`), and adds `0` since it's even
    - `answer[0 >> 1] + 0 % 2 = 0`
2. `number = 1`: answer equals that of `0` (`1 >> 1 = 0`), and adds `1` since it's odd
    - `answer[1 >> 1] + 1 % 2 = 1`
3. `number = 2`: answer equals that of `1` (`2 >> 1 = 1`), and adds `0` since it's even
    - `answer[2 >> 1] + 2 % 2 = 1`
4. `number = 3`: answer equals that of `1` (`3 >> 1 = 1`), and adds `1` since it's odd
    - `answer[3 >> 1] + 3 % 2 = 2`
5. `number = 4`: answer equals that of `2` (`4 >> 2 = 2`), and adds `0` since it's even
    - `answer[2 >> 1] + 2 % 2 = 1`
6. `number = 5`: answer equals that of `2` (`5 >> 1 = 2`), and adds `1` since it's odd
    - `answer[5 >> 1] + 5 % 2 = 2`

## Results (Python 3)

**Method 1**:  198 ms, 20.7 MB (23.22%, 80.59%)

**Method 2**:  142 ms, 21.0 MB (43.14%, 5.39%)

**Method 3**:  102 ms, 20.9 MB (72.13%, 31.30%)

## Lessons Learned
1. Draw it out:  binary problems have patterns that can be seen easily if the bitwise representations are listed.
2. Use tables: whip up quick tables of inputs, outputs, and variable values at particular steps of the program.
3. Check your constraints: one of my earlier solutions failed because it didn't account for `n <= 100,000`.
4. Refine the process: look for patterns in your solutions to streamline the answer into a more flexible and elegant algorithm.  This one had a very obvious pattern using *base 2* (`2^0, 2^1, 2^2, ...`).
