# Valid Palindrome ([LC125](https://leetcode.com/problems/valid-palindrome/))
Difficulty: **Easy**

## Problem

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a ***palindrome***, or `false` otherwise.

Constraints:
- `1 <= s.length <= 2 * 10⁵`
- `s` consists only of printable ASCII characters.

## Thought Process

Alphanumeric characters are `a-z`, `A-Z` and `0-9`.

Edge Cases / Caveats / Pitfalls:
- String of length `0` -> N/A by constraints
- String of length `1` -> automatically a palindrome
- String that reduces to empty string `""` -> automatically a palindrome
- UPPER case characters
- Whitespace characters
- Symbolic characters like `:`, `,`, etc.

Approaches:
1. Converging iteration: start at *both ends* of the string `s` and ensure that both letters at each iteration point match.  Can stop if you meet halfway, since a palindrome will be symmetrical.
2. Reverse and compare: reverse string `s`, then compare each letter one-by-one

## Procedure

### Method 1: Converging Iteration w/Pre-Processing

Key Steps:
1. Pre-process the input `s` into a `new_string` with the following steps:
    - keep only alphanumeric characters
    - convert all alphanumeric characters to lower case
2. Create two iterators: a forward iterator from `start->end` and a reverse iterator from `end->start` in string `s`.
3. One by one, compare characters `c1` (forward) and `c2` (reverse) in each iterator:
    - if `c1 == c2`, continue
    - if `c1 != c2`, return `false`
4. If all comparisons complete without returning `false`, return `true`.

Thoughts:
- Python's `str` methods and iterators make this problem pleasant to work with, as long as you're familiar with them.

## Results (Python 3)

**Method 1**:  69 ms, 14.18 MB (45.15%, 33.62%)
