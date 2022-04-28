# Valid Anagram ([LC242](https://leetcode.com/problems/valid-anagram/))
Difficulty: **Easy**

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Constraints:
- `1 <= s.length, t.length <= 5 * 104`
- `s` and `t` consist of lowercase English letters.

## Procedure

### Method 1: DefaultDict Counter

This was another case where Python's `defaultdict` comes in handy.  To see if `t` is an anagram of `s`, simply check for all cases that would make it *not* an anagram.  If those test cases pass, then `t` is a valid anagram of `s`.  

`t` is *not* an anagram of `s` if *ANY* of the following are true:

1. `s` and `t` are of different lengths
2. any letter in `t` is not in `s`
3. any letter in `s` is not in `t`
4. `t` has a surplus or deficit of letters that are in `s`

## Results (Python 3)

**Method 1**:  57 ms, 14.4 MB (69.03%, 97.46%)
