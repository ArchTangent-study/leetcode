# Combination Sum II ([LC040](https://leetcode.com/problems/combination-sum-ii/))
Difficulty: **Medium**

## Problem

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find *all unique combinations in* `candidates` *where the candidate numbers sum to* `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note**: The solution set must not contain duplicate combinations.

Constraints:
- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Duplicate combinations

## Procedure

### Method 1: Dynamic Programming w/Dictionary Counter

Big Picture:
1. Use `numbers` dictionary to count and deduplicate `candidates`
2. Iterate over each `number` and `count` in `numbers`
3. Iterate over each `multiple` in `count` (starting from `1` to c`ount + 1`)
4. Set `product` to `number * multiple` (e.g. `3 * 1 = 1`; `3 * 2 = 6`)
5. Compare product vs all combinations whose sums are less than target:
    - if `product + combination == target`, add new combination to `answer`.  Example: `number = 3, multiple = 2, combo = [1,2] -> new combo = [1,2,3,3]`
    - if `product + combination > target`, move to next number
    - if `product + combination < target`, add new combination to `combination` list.
6. Return `answer`

Complexity:
- Time: explore all possible combinations `c` -> `O(c)`,
- Space: store temporary `combinations` list for each `n` -> `O(c * n)` (???)

Where:
- `c` is number of possible combinations
- `n` is number of candidates

## Results (Python 3)

**Method 1**: 62 ms, 13.9 MB (**89.90%**, **93.01%**)
