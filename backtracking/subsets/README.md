# Subsets ([LC078](https://leetcode.com/problems/subsets/))
Difficulty: **Medium**

## Problem

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Empty `nums`: N/A as per constraints
- Single number: return `[[], [number]]`
- Accounting for empty member of power set

Approaches:
- Brute force: all numbers are either present or not -> `O(2ⁿ)`

## Procedure

### Method 1: Iterative DP

Big Picture:
1. Store `answer` pre-stored with empty pair, `[[]]` for full power set
2. Store a `to_add` list for all new incoming merges
3. Ierate over all `n` in `nums`
4. Gather all existing values from `answer` into a `to_add` and merge with `n`
    - if value is `[5]` and `n = 3`, merge into `[5,3]`
    - if value is `[1,2]` and `n = 3`, merge into `[1,2,3]`
5. Extend all values in `to_add` into `answer` and clear `to_add`
6. return `answer` once iteration complete

Complexity:
- Time: iterate each `n` in `nums` once and merge w/all other combinations -> `O(2ⁿ)`
- Space: separate `to_add` holds all previous values of `answer` > `O(2ⁿ)`

### Method 2: Recursive DFS

Visualization:
```
ix 0 (1)                   [1]                             []
ix 1 (2)           [1,2]          [1]               [2]             []
ix 2 (3)    [1,2,3]        [1,2]       [1]  [2,3]           [2]             []
ix 3                    (end - append all individual subsets to answer)
```

Big picture:
1. Account for two different paths, `left` and `right`:
    - `left`: `number` at `index` in `nums` is merged into given `subset`
    - `right`: no merge - copy of `subset` is passed on unchanged
2. Perform Depth-First Search (DFS) on both the `left` and `right` side, increasing `index` by `1` each time.
3. When `index` goes out of bounds, add all individual subset to the `answer`.

Complexity:
- Time: `O(2ⁿ)`
- Space: `2ⁿ` intermediate subsets added to `answer` -> `O(2ⁿ)`

## Results (Python 3)

**Method 1**: 66 ms, 14.1 MB (17.00%, 81.00%)

**Method 2**: 29 ms, 14.1 MB (**98.56%**, 81.00%)
