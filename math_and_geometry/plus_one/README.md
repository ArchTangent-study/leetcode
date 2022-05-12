# Plus One ([LC066](https://leetcode.com/problems/plus-one/))
Difficulty: **Easy**

## Problem

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `ith` digit of the integer. The digits are ordered from most significant to least significant in *left-to-right* order. The large integer does not contain any leading `0`s.

Increment the large integer by one and return the *resulting array of digits*.

Constraints:
- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` does not contain any leading `0`s.

## Thought Process

Key Ideas:

Layout is as follows, where MSD/LSD are most/least significant digits:
```
      MSD LSD
124 = [1,2,4]
```

Edge Cases / Caveats / Pitfalls:
- Where the least significant digit is `9`
- Any other instances where digit is `9` and must be incremented ("carried")
- At end of iteration and a "carry" is still active (e.g. `999 -> 1000`)
- Preserving order of digits during iteration - be sure not to reverse the digits!
- Knowing when to stop iteration.

Approaches:
1. Use a "carry" value: if LSD is `9`, store a `carry = true` or `carry = 1` value that is sent to next bit, used to increment it.  Repeat until carry is exhausted.
2. Recursion: iterate over `digits`, adding each digit to `answer`, and passing any carries back to the caller.

## Procedure

### Method 1: Reverse Iterate and Carry

The Steps:
1. Store `answer = list()` and `carry = 1`.
2. Iterate `digits` in reverse. For each `digit` in `digits`:
    - if it is `< 9`, push `digit + 1` to `answer` and set `carry = 0`
    - if it is `9`, push `0` to `answer`  and set `carry = 1`
3. At the end of iteration, check `carry`
    - if it is `1`, push `1` to `answer`
4. Return `answer` ***in reverse***

Visualization:
```
Digits = 123
        digit  answer  carry
start                    1      always start with carry = 1
step 1    3     4        0      append 3+1 to answer, set carry = 0
step 2    2     42       0
step 3    1     421      0
step 4          421      0      End of iteration and carry = 0 -> do nothing
result          124      0      Reverse answer and return

Digits = 999
        digit  answer  carry
start                    1      always start with carry = 1
step 1    9     0        1      digit is 9 -> append 0 to answer, set carry = 1
step 2    9     00       1      digit is 9 -> append 0 to answer, set carry = 1
step 3    9     000      1      digit is 9 -> append 0 to answer, set carry = 1
step 4          0001     1      End of iteration and carry = 1 -> append 1 to answer
result          1000     1      Reverse answer and return
```

## Results (Python 3)

**Method 1**: 32 ms, 13.9 MB (91.15%, 60.22%)
