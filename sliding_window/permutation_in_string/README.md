# Permutation in String ([LC567](https://leetcode.com/problems/permutation-in-string/))
Difficulty: **Medium**

## Problem

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

Constraints:
- `1 <= s1.length, s2.length <= 10⁴`
- `s1` and `s2` consist of lowercase English letters.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Out of bounds errors
- Counting all permuations `abc, acb, bac, bca, cab, cba`
- Slice indexing (`[0:2]` covers indexes `0` and `1`, not `2`)

## Procedure

### Method 1: Two Pointers Sliding Window w/Dict Counter

Key Idea: each permuation of `s1` can be found by *matching the* ***count*** *of each letter in the string*.  This is the same as working with *anagrams*.

Visualization:
```python
s1 = "ab"; s2 = "eidbaooo"; count = {'a': 1, 'b': 1}

"eidbaooo"        
 ^^          'e': 1, 'i': 1
  ^^         'i': 1, 'd': 1
   ^^        'd': 1, 'b': 1
    ^^       'b': 1, 'a': 1 <- found

return True
```

Big Picture:
1. Start with a two-pointer window of span `len(s1)` with `p1` at index `0` and `p2` at index `len(s1)` of `s2`.
2. Check for permutation at each position by checking the *count* of each letter in the window (e.g. `{"a": 1, "b": 1}`) against the count within the window.
3. Slide the window to the right until:
    - permutation is found -> return `True`
    - `p2` (right pointer) exceeds of `len(s2)`

Complexity:
- Time: check `n` (in `s2`) windows with up to `26` pairs -> `O(26n)` -> `O(n)`
- Space: up to `26` pairs (see constraints) in each dictionary -> `O(1)`

*Note*: this can be made faster by not constructing a new `dict` for each window.  Instead, re-use the same `dict` and update the `count` of each letter *leaving* and *entering* the window.

## Results (Python 3)

**Method 1**:  ms,  MB (%, %)
