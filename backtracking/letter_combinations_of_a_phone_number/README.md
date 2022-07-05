# Letter Combinations of a Phone Number ([LC017](https://leetcode.com/problems/letter-combinations-of-a-phone-number/))
Difficulty: **Medium**

## Problem

Given a string containing digits from `2-9` inclusive, return *all possible letter combinations that the number could represent*. Return the answer in **any order**.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that `1` does not map to any letters.

Constraints:
- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- `1` doesn't map to a letter.
- Same digit repeated (not an issue since this is a combination)

## Procedure

### Method 1: Iteration

Key Ideas:
- Early exit if `digits` is empty
- Store `map` of `{ digit : chars_in_digit }` for easy access
- Use temporary arrays to update existing `answer` in-place

Complexity:
- Time: max of `4` chars per `n` in digit, traversed `n` times -> `O(n * 4ⁿ)`
- Space:  answer stored in `temp` list before added to answer -> `O(n * 4ⁿ)`

## Results (Python 3)

**Method 1**: 36 ms, 14.0 MB (79.25%, 29.91%)
