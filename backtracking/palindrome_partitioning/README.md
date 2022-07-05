# Palindrome Partitioning ([LC131](https://leetcode.com/problems/palindrome-partitioning/))
Difficulty: **Medium**

## Problem

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return *all possible palindrome partitioning of `*s`.

A **palindrome** string is a string that reads the same backward as forward.

Constraints:
- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- `s` length is `1` -> return `[s]`
- getting all substrings (`['a', 'a']` differs from  `['aa']`)
- avoiding empty strings (don't count toward answer)
- avoiding duplicates

Key steps:
- Getting substrings
- Finding substrings that are palindromes
- Getting partitions
- Returning partitions that are composed entirely of palindromic substrings

## Procedure

### Method 1: Recursion w/DFS

Visualization for `"aab"`:
```
            "a","ab"                "aa","b"              "aab",""
           /   \                    /                      /
       "a","b"  "ab",""          "b",""                (invalid)
        /         \              /
     "b",""     (invalid)    ["aa","b"]    
      /
["a","a","b"]    
```

Big Picture:
1. Divide all strings into partitions using `incoming` and `remainder` values
    - e.g.  `"aab" -> "a","ab" ; "aa","b" ; "aab",""`
2. for each partition, check if it is a palindrome
    - if it is not, early exit
    - if it is, add incoming to a list of substrings so_far
        - if all substrings in so_far combine to equal input string, return so_far
    - recursively call `dfs()`, partitioning `remainder` into *new* `incoming/remainder`

Complexity:
- Time:  `O(n * 2ⁿ)`
- Space: store list copies of max length `n` -> `O(n)`

## Results (Python 3)

**Method 1**: 859 ms, 31.4 MB (62.61%, 13.78%)
