# Group Anagrams ([LC049](https://leetcode.com/problems/group-anagrams/))
Difficulty: **Medium**

## Problem

## Thought Process

Questions:
- Are all strings in input the same length?  Examples show that they are.

Edge Cases / Caveats / Pitfalls:
- Case sensitivity:  all lowercase `a-z` as per the constraints.
- Sorting strings in Python
- Empty list: return empty list
- Empty string: return empty string
- Single string: return the string

Tips:
- Convert a python character into its ASCII code with `ord(char)` built-in function.
- Convert a ASCII code into a python character with `chr(ord)` built-in function.
- Sort a string by using `''.join(sorted(string))`

## Procedure

### Method 1: Sort and Hash

Key Idea: A word `W1` is an anagram of word `W2` if they are the same word when ***sorted alphabetically***.

Steps:
1. Create a table `{str: list(str)}` of `matches`.
2. Iterate over each `string` in `strs`.
3. Sort the `string` alphabetically to get `sorted_string`.
4. Add `string` to the list of matches under `matches[sorted_string]`.
    - if `sorted_string` is not in `matches`, add the key first
5. Iterate over all values (lists) in `matches`, and collect into a `result` list.
6. Return `result` list.

Complexity:
- Time: use quicksort to sort each string `O(n log n)`
- Space: at worst, one dictionary entry per string -> `O(n)`

### Method 2: Count and Hash

Key Idea: A word `W1` is an anagram of word `W2` if they have the ***same count of letters a-z***.  This assumes all strings have been converted to *lowercase*, which is true as per the constraints.

Caveats:
- when converting `a-z` into numbers using `ord()`, you need to iterate from `ord(a)` to `ord(z) + 1` to include `z`.  Using `ord(z)` as the end range will only include letters from `a-y`.

Complexity:
- Time: `O(n)`
    - `26` letters per `letter_count` dict & tuple -> constant -> `O(1)`
    - traverse `m` strings and `n` lettters per string -> `O(n)`
- Space: `O(n)`
    - `26` letters per `letter_count` dict & tuple -> constant -> `O(1)`
    - up to `n` strings stored in each dictionary `O(n)`

Thoughts:  even though this has better time complexity than Method 1, this performed *far* worse when run on LeetCode.

## Results (Python 3)

**Method 1**: 99 ms, 17.1 MB (**94.44%**, **96.49%**)

**Method 2**: 295 ms, 19.0 MB (5.02%, 31.88%)
