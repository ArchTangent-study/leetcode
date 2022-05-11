# Happy Number ([LC202](https://leetcode.com/problems/happy-number/))
Difficulty: **Easy**

## Problem

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
- Those numbers for which this process **ends in 1** are happy.

Return `true` if `n` is a happy number, and `false` if not.

Constraints:
- `1 <= n <= 2³¹ - 1`

## Thought Process

While brute force might work, there is likely some way to streamline the process:
- mathematical property that makes it easy to determine if a number is or isn't happy
- tables of digits `0` to `9` with "happy" pairs
- identifying and/or caching *repeated patterns*

I did some testing to see what patterns would emerge from calling `isHappy()` on numbers `0` to `29` while setting an upper limit to `20` tries (to avoid endless loops).  

The initial values of `n` that *were* happy within `20` tries were `1, 7, 10, 13, 19, 23, 28`.

The initial values of `n` that were *not* happy within `20` tries were `2, 3, 4, 5, 6, 8, 9, 14, 15, 16, 17, 18, 20, 21, 22, 24, 25, 26, 27, 29`.

The values of `n` that showed up for non-happy numbers included `16, 20, 37, 42, 58, 89, 145`, and many of them appeared *repeatedly*.  This indicates an *underlying pattern*.

A table of happy and unhappy numbers from start to finish:
```
        Happy                   Unhappy
7   10  13  19  23  28          2   3     
49  1   10  82  13  68          4   9       
97      1   68  10  100         16  81
130         100 1   1           37  65
10          1                   58  61
1                               89  37
                                145 58
                                42  89
                                20  145
                                4   42
                                ... 20
                                    4
```

Patterns noticed:
- Since numbers are 32-bit unsigned integers, the maximum number has 32 `9`s, and its sum of squares would be `32 * (9*9) = 2592`
- Happy cases end up at a point where they have a **single 1 and any number of 0 digits**.  This way, the sum of squares is always `1`.
- Unhappy cases included many of the same numbers showing up *repeatedly*. If these numbers are encountered, the initial number `n` is *doomed* to be unhappy.
- More importantly, unhappy cases all reached a point where they reached the **same value twice**.  Once that happens, a loop is **guaranteed**.  In the above example, both   `2` and `3` encountered the number `4` twice.

Using the above patterns, we now have the two base cases necessary to determine happy/unhappy numbers.

Edge Cases / Caveats / Pitfalls:
- Infinite loops: need a way to prevent them.  Either set a cap on number of runs, or identify a recurring pattern and exit early *preferred*.

Key Ideas for `sumOfSquares()`:
- Extract the rightmost digit by using `digit = n % 10`
- Shift a decimal number right by using `n = n // 10`

## Procedure

### Method 1: Unhappy Set

Big Picture:
- Store a set of known unhappy numbers
- Use as small a set as possible
- Once `n` is in that set, it is doomed to be unhappy

Algorithm:
1. Create set of `bad_numbers`, holding digits `< 10` that are known to lead to an unhappy state:  `{2, 3, 4, 5, 6, 8, 9}`
2. Peform `sumOfSquares(n)`
3. If `n == 1`: return `True`
4. If `n in bad_numbers`: return `False`
5. Repeat from step `2` until a happy or unhappy number is found.

Thoughts:
- Since `2 * 2 = 4` and `3 * 3 = 9`, you could remove both `2` and `3` (or `4` and `9`) from the set of `bad_numbers` for an even smaller set  of `{4, 5, 6, 8, 9}`.

### Method 2: Repetition Check

As shown in the *Thought Process* section above, there's a point in every unhappy number where it repeats itself.  This can be used as an exit condition.

Algorithm:
1. Create an empty set of `repeat_numbers`
2. If `n == 1`: return `True`
3. Peform `sumOfSquares(n)` to calculate new `n`
4. If new `n` is already in `repeat_numbers`, return `False` (repeat).
5. Repeat from step `2` until a happy or unhappy number is found.

## Results (Python 3)

**Method 1**: 35 ms, 13.8 MB (88.01%, 61.63%)

**Method 2**: 42 ms, 13.8 MB (65.56%, 97.13%)
