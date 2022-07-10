# Minimum Window Substring ([LC076](https://leetcode.com/problems/minimum-window-substring/))
Difficulty: **Hard**

## Problem

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the ***minimum window substring*** of `s` such that every character in `t` (***including duplicates***) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is **unique**.

A **substring** is a contiguous sequence of characters within the string.

Constraints:
- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10⁵`
- `s` and `t` consist of uppercase and lowercase English letters.

## Thought Process

Notes:
- 52 possible characters `"a-z,A-Z"` in the input

Edge Cases / Caveats / Pitfalls:
- OOB errors
- Multiple instances where substring occurs, but need the smallest.
- Approaching answer from left and right side (two passes?)
- Modifying a character count more than once

Approaches:
- Tightening window: start at entire span, then shrink span using L/R pointers to the smallest span that contains the required characters.  Effectively, shrink until the span can be shrunk no further.
- Alternating shrinking:  bring in L/R pointers in alternating fashion.
- Find most extreme index at which each character is satisfied, e.g for `"ABEECEBA"`:
    - `leftmost  = { "A": 0, "B": 1, "C": 4 }`
    - `rightmost = { "A": 7, "B": 6, "C": 4 }`
    - answer = `"CEBA"` from indexes `4` to `7` (not `"ABEEC"` from ixs `0` to `4`)
- Two passes: to guarantee correct answer from L/R side

## Procedure

### Method 1: Two Pointer Sliding Window - Two Pass

Key Ideas:
- Use two passes: one to look for the *first* answer (if any, early exit otherwise), two to progressively scan for smaller windows containing *better* answers.
- To count as a valid answer, each count in `chars_required` must be `0` or less.  In other words, each valid substring in `s` must have *at least* ***all*** the letters in `t` (can have more).

Visualization
```python
s = "ABEECEBA"; t = "ABC"; chars_required = { "A": 1, "B": 2, "C": 3 }

ABEECEBA       A  B  C  
A              0  1  1   
AB             0  0  1 
ABE            0  0  1
ABEE           0  0  1
ABEEC          0  0  0  Found first answer "ABEEC". Shift p1 right.
 BEEC          1  0  0 
  EECE         1  1  0 
   ECEB        1  0  0 
    CEBA       0  0  0  Found second answer "CEBA". Shift p1 right.
     EBA       0  0  1  
      BA       0  0  1  p2 - p1 span of 2, < len(t).  Stop

return "CEBA"
```

Big Picture:
1. Gather requirements: `chars_required` dict of `{ char : count }` pairs, where valid answers need `count` to be *less than `1`*  for each `char`.
2. Find *first* answer: iterate over each `char` in `s`:
    - set left pointer `p1` to the *first* instance of a *required* `char`
    - set left pointer `p2` to *each* instance of a *required* `char` until the *first*  valid answer is found
3. If no first answer was found, return empty string `""`
4. If first answer was found, shrink window by moving `p1` to the right, and start 2nd pass to find *better* (smaller) answers.
5. As long as as `p2 - p1` is wide enough to hold the smallest possible answer:
    - check if `s[p1:p2+1]` has an answer.  If so, update `answer` and shift `p1` right
    - If no answer, shift `p1` and `p2` to the right making sure *not* to shift `p2` if it's already at the final index in `s`
6. Return the most recent `answer`, as this will be the smallest.

Complexity:
- Time: for each of `n` chars in `s`, check up to `t` (max `52`)  chars -> `O(52n)` -> `O(n)`
- Space: up to `t` (max `52`) chars in `dict` -> `O(1)`

*Note*: this can be made faster by only checking for a new valid answer (by checking that the `count` of each `char_required < 1`) when the `count` rises above `0` when sliding left pointer `p1` to the right.

## Results (Python 3)

**Method 1**: 29.87 ms, 14.6 MB (29.87%, **82.88%**)
