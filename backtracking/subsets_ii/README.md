# Subsets II ([LC090](https://leetcode.com/problems/subsets-ii/))
Difficulty: **Medium**

## Problem

Given an integer array `nums` that may contain duplicates, return *all possible subsets (the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

Constraints:
- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Duplicate subsets
- Returning empty subset (`[]`)
- Single number in `nums` -> (`[], [number`)
- Non-unique numbers in `nums`

## Procedure

### Method 1: Dynamic Programming w/Set and Counter

Key Idea: need to (a) deduplicate and (b) count occurrences of each `number` in `nums` for this to work.

Big Picture:
1. Use a `set` to deduplicate multiple instances of numbers
2. Track the `count` of each number's occurrence
3. Start with an empty subset (`[]`) in `answer`
4. For each `number` in `nums`:
    - get each `subset` in `answer`
    - for each `count` of the `number` (e.g. `1,2,3,...`):
        - make new subset by inserting number into a copy of that subset
        - append new subset to a `staging` area
    - at end of each `number`, add `staging` area to `answer`
    - clear `staging` area
5. Return the `answer`

Complexity:
- Time:  up to `2ⁿ` subsets -> `O(2ⁿ)`
- Space: `staging` list can have up to `2ⁿ` items -> `O(2ⁿ)`

## Results (Python 3)

**Method 1**: 48 ms, 14.1 MB (73.17%, 48.81%)
