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

### Method 1: Iterative Deduplication

Big Picture:
1. Store `answer` pre-stored with empty pair, `[[]]` for full power set
2. Store a `set` of ints/tuples for all combinations
3. Ierate over all `n` in `nums`
4. Gather all existing values from `set` into a `list` and merge with `n`
    - if value is `5` and `n = 3`, merge into `(5,3)`
    - if value is `(1,2)` and `n = 3`, merge into `(1,2,3)`
5. Add merged values, e.g. `(n, *values)` to `set`
6. add `n` to `set`
7. Extend all values in `set` into `answer` and return `answer`

Complexity:
- Time: iterate each `n` in `nums` once and merge w/all other combinations -> `O(2ⁿ)`
- Space: separate `set` holds the power set before adding to answer -> `O(2ⁿ)`

Thoughts: this was surprisingly fast considering it was the first idea that came to mind.

## Results (Python 3)

**Method 1**: 39 ms, 14.3 MB (83.74%, 33.77%)
