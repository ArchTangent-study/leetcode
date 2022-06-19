# Encode and Decode Strings ([LC271](https://www.lintcode.com/problem/659/))
Difficulty: **Medium**

*Note*: this is a LeetCode premium question, also available via `LintCode` problem `659`.

## Problem

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement `encode` and `decode`.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Strings that use the same characters as your delimiter (e.g. `delimiter == '32#'` and `string == "#wow#ie"`)
- Strings that use digits that might appear in delimiter (e.g. `delimiter == '2#'` and `string == "2#1337#4u"`)

## Procedure

### Method 1: Prefix Delimiter w/ Two Contexts

The trick to this problem is finding a delimiter that won't conflict with any characters in a word you're en/decoding.  The best way I came up with is to use a *prefix* ensuring that you can know the number of characters in any word *in advance*, avoiding conflicts.

Encoding:  use a `'dd#'` *prefix* delimiter, where:
- `d` is a character in the digit *length* of the *upcoming string*.  E.g. `25` means that the next string will be `25` characters long.
- `#` is the delimiter *terminator*, which indicates that the length of the upcoming string has been fully gathered.  E.g. `3#` means that the next string will be `3` characters long.

Decoding:  alternates between two contexts:
1. **Delimiter context**: gather the length of the next string untl delimiter *terminator* is found.
2. **Word context**: gather characters for the decoded string.

The rest of the process is explained in the code.

Complexity:
- Time: traverse each character once per encode/decode pass -> `O(n)`
- Space: store two strings for each word before added to ouput -> `O(n)`

### Alternative

Keep a `start` and `end` pointer (*Two Pointer* approach) to reduce space complexity to `O(1)`

## Results (Python 3)

**Method 1**: 612 ms, 6.08 MB (31.20%) *via LintCode*
