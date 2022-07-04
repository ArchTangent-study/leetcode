# Word Search ([LC079](https://leetcode.com/problems/word-search/))
Difficulty: **Medium**

## Problem

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` *exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Constraints:
- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters.

Follow-up: use [search pruning](https://en.wikipedia.org/wiki/Decision_tree_pruning) to find a solution faster.

## Thought Process

Questions:
- Does case matter for determining if `word` is present?  `SEEK` vs `seek`.

Edge Cases / Caveats / Pitfalls:
- Can't use same cell twice
- Can only check in NSEW directions
- Bounds checks
- Searching `word` in forward *and* backward direction (e.g. word `seeks` has `s` at both ends)
- Pruning too early (as in word `seeks`)

## Procedure

### Method 1: Recursive DFS w/ Preliminary Filtering

Key Idea: perform a *filter pass* on the `board` before searching for the `word`.  This "prunes" the amount of eligible tiles to search.

Big Picture:
1. Collect all letters in word as a set.
2. Filter the `board`:
    - add `(row,col)` `coords` for letters not in `word` to an `ignored` set
    - add `(row,col)` `coords` for letters starting word in `start_tiles` list
3. For every set of `coords` in `start_tiles`, perform DFS to see if `word` is found
4. if `word` was found, return `True`
5. if `word` wasn't found for any starting point, return `False`

Complexity:
- Time: four directional search, no tiles filtered -> `O(4ⁿ)` (???)
- Space: sets to hold all `word` letters and `ignored` tiles -> `O(w + n)`

Where:
- `w` is `word` length
- `n` is the number of `tiles` in `board` (rows * columns)

### Method 2: Recursive DFS w/ Preliminary Filtering and Early Exit

Same as Method 1, except: don't even search for the `word` if `board` doesn't have enough letters to contain `word`.  Do this by:
    - count occurrences of each letter in `word`
    - decrement letter's count by `1` each time letter is found in `board`
    - if the count for *any* letter is `>1` after entire `board` is searched, the `word` *cannot* be present in `board` -> return `False` without searching.

This wound up being ***twice as fast*** as Method 1 by avoiding unnecessary searches.

## Results (Python 3)

**Method 1**: 5444 ms, 13.9 MB (81.26%, 50.67%)

**Method 2**: 2427 ms, 14.1 MB (**95.33%**, 12.16%)
