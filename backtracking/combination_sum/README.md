# Combination Sum ([LC039](https://leetcode.com/problems/combination-sum/))
Difficulty: **Medium**

## Problem
Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of all unique combinations of candidates where the *chosen numbers sum to* `target`. You may return the combinations in **any order**.

The same number may be chosen from candidates an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than `150` combinations for the given input.

Constraints:
- `1 <= candidates.length <= 30`
- `1 <= candidates[i] <= 200`
- All elements of `candidates` are **distinct**.
- `1 <= target <= 500`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- A number equal to `0` (allows multiple answers) -> N/A as per constraints
- Same number being used repeatedly

Approaches:
- Sorting
- DP
- Recursion

## Procedure

### Method 1: Iterative DP

Visualization:
```
candidates = [3,5,8]; target = 11
     v
    [3,5,8]         inclusive pass for 3: counted from 1 to (11/3) = 3 times
                      5 is counted from 0 to (11/5) = 2 times (optional pass)
                      8 is counted from 0 to (11/8) = 1 times (optional pass)
                    adds all combinations that:
                        - equal `target`
                        - include `3`
       v
    [3,5,8]         inclusive pass for 5: counted from 1 to (11/5) = 2 times
                      3 is NOT INCLUDED - already had its inclusive pass
                      8 is counted from 0 to (11/8) = 1 times (optional pass)
                    adds all combinations that:
                        - equal `target`
                        - include `5`
                        - exclude `3`
         v
    [3,5,8]         inclusive pass for 8: counted from 1 to (11/8) = 1 times
                      3 is NOT INCLUDED - already had its inclusive pass
                      5 is NOT INCLUDED - already had its inclusive pass
                    adds all combinations that:
                        - equal `target`
                        - include `8`
                        - exclude `3` and `5`
```

Big Picture: each `candidate` is subject to two passes:
1. Inclusive pass: `candidate` is included `1` *or more* times
    - this is done at the top level, as candidates is iterated over
2. Optional pass: `candidate` is included `0` *or more* times
    - this is done within a recursive call of `combo()` for every number after the *inclusive* `candidate`
Additionally includes:
- exclusion: once a `candidate` has had its inclusive pass, it is not checked again.
- early exit: stop when the `running_sum` has exceeded `target` - no need to look further
- no duplication: each combination is checked ***only once***.  Once `3` in `[3,5,8]` has its inclusive pass, it is not used in any other inclusive pass (for `5` and `8`)

Complexity:
- Time: -> `O(2^t)`
- Space: up to `t` `candidates` stored in a temporary `subset` -> `O(t)`. This is the worst case *longest combination* you could have, and could occur with `candidates = [2]` and `target = 8` resulting in `[2,2,2,2]` as the final answer (where `t = 4`).
Where:
- `n` is number of `candidates`
- `t = sum(target / candidate)` for each `candidate` in `candidates`):

## Results (Python 3)

**Method 1**: 171 ms, 14.1 MB (24.33%, 23.54%)
