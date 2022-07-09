# Longest Repeating Character Replacement ([LC424](https://leetcode.com/problems/longest-repeating-character-replacement/))
Difficulty: **Medium**

## Problem

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the *length of the longest substring containing the same letter you can get after performing the above operations*.

Constraints:
- `1 <= s.length <= 10⁵`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

## Thought Process

Notes:
- Only need to include letter that are already in `input` string
- Reflexivity:  changing all `B`s to `A`s would be the same as changing all `A`s to `B`s
- if `k` >= `len(s)`, return `len(s)`
- if only one letter in `s`, return `len(s)`
- `k = 0`: just get the longest repeating character length
- if two letters `s`, and `k` > count of either letter, return `len(s)`

Edge Cases / Caveats / Pitfalls:
- Accounting for all combinations
- Replacing characters at *beginning* and *end* of string
- Accounting for replacement in **both directions** (L to R, R to L)

Ideas:
- Using `ord(char)` to store counts in a `list` vice a `dict`, e.g. `count[ord("B") - ord("A")] += 1` to increment the count for `"B"`.

## Procedure

### Method 1: Two Pointer Sliding Window

Key Ideas:
- If the count of the most common character in a span (e.g. `3 "A"`s in `"AABBA"`) plus `k` is `>=` the width of `span`, there is sufficient `k` to make all replacements.
- The actual character doesn't make a difference (`"A"`, `"B"`); only the *count* of the most common character does.

Visualization for `"ABAB", k=0`:
```
ABAB  A B S
^     1 0 1 
^^    1 1 2*    2 is higher than max span of 1
 ^    0 1 1     left pointer advances to bring span back to 1
 ^^   1 1 2*    2 is higher than max span of 1
  ^   1 0 1     left pointer advances to bring span back to 1
  ^^  1 1 2*    2 is higher than max span of 1
   ^  0 1 1     left pointer advances to bring span back to 1

Right pointer reaches end -> max valid span is 1
```

Complexity:
- Time: traverse up to `26 dict` pairs for every `n` in input -> `O(26n)` -> `O(n)`
- Space: up to `26` `character:count` pairs in `dict` -> `O(1)`

## Results (Python 3)

**Method 1**: 180 ms, 14.0 MB (66.34%, 57.98%)
