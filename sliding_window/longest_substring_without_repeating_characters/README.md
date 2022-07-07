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
- Words with multiple duplicate characters

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
- Time: every char visited `1 + 2 + 3 + ... n` times (e.g. `"abcdef"`) -> `O(n²)`
- Space: `set` holds *known maximum* number of possible characters -> `O(1)`

### Method 2: Sliding Window w/Hashmap

Key Idea: use hashmap to (a) find repeat characters and (b) store indexes to track the start of the next substring to be tested.

Visualization for `"dvdf"`:
```python
 char_map                   substring  start_ix  max_length
{ "d": 0 }                    "d"         0         0
{ "d": 0, "v": 1 }            "dv"        0         0
{ "v": 1, "d": 2 }            "vd"        1         2
{ "v": 1, "d": 2, "f": 3 }    "vdf"       1         2

end of iteration
return max(max_length, len(s) - start_ix)
return max(2, 4 - 1)
return 3
```

Complexity:
- Time: every char visited once -> `O(n)`
- Space: `dict` holds *known maximum* number of possible characters -> `O(1)`

### Method 3: Two-Pointer Sliding Window w/Set

Similar to Method 2, but differs by:
- using two pointers instead of iteration
- using a `set` instead of a `dict`

Complexity:
- Time: chars visited at worst 2x (e.g. `"ababab"`) -> `O(2n)` -> `O(n)`
- Space: `set` holds *known maximum* number of possible characters -> `O(1)`

## Results (Python 3)

**Method 1**: 734 ms, 14.1 MB (10.92%, 49.44%)

**Method 2**: 550 ms, 14.1 MB (13.91%, 49.47%)

**Method 3**: 71 ms, 14.1 MB (**84.57%**, 49.47%)
