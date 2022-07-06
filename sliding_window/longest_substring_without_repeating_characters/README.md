# Longest Substring Without Repeating Characters ([LC003](https://leetcode.com/problems/longest-substring-without-repeating-characters/))
Difficulty: **Medium**

## Problem

Given a string `s`, find the length of the **longest substring** without repeating characters.

Constraints:
- `0 <= s.length <= 5 * 10⁴`
- `s` consists of English letters, digits, symbols and spaces.

## Thought Process

*Note*: be sure to *read the question carefully*. I first thought that the problem considered a character to be repeating if two or more consecutive characters were the same.  That is *not* the case.

Edge Cases / Caveats / Pitfalls:
- Empty string: return `0`
- String of length `1`: return `1`

## Procedure

### Method 1: Naive Iteration w/Set Deduplication

Key Idea: try each substring from `s[0:]` to `s[-1:]` and collect longest valid substring length.

Big Picture:
1. Keep a `max_count` (overall) and a `current_count` (current pass) value.
2. Iterate starting from every `char` in `s`, e.g. `"f"`, `"u"`, and `"n"` in `"fun"`
3. For each `char` in the iteration, check it vs the set.
4. If `char` is not in the set:
    - add each `char` to the set and increment `current_count`
5. If `char` is in the set:
    - update `max_count` with highest of itself and `current_count`
    - reset `current_count` to `0` and clear the set
6. Return `max_count`

Complexity:
- Time: every char visited twice in worst case, e.g. `"sasasasa"` -> `O(2n)` -> `O(n)`
- Space: `set` holds *known maximum* number of possible characters -> `O(1)`

## Results (Python 3)

**Method 1**: 734 ms, 14.1 MB (10.92%, 49.44%)
