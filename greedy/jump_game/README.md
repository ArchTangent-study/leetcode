# Jump Game ([LC055](https://leetcode.com/problems/jump-game/))
Difficulty: **Medium**

## Thought Process

Questions:
- Does a single index (even if `0`) constitute reaching the last index? Assume *yes*.

Edge Cases / Caveats / Pitfalls:
- zero jump size
- multiple zeroes
- insufficient jump length at later step, but sufficient at earlier step

## Procedure

### Method 1: Backtracking

Big Picture: work backward from finish, starting with `0` required jump distance.

Steps:
1. Starting from last index, iterate backward.  For each `jump` in `nums`:
    - if `jump < required`: add `1` to `required`
    - if `jump >= required`: reset `required` to `1`
2. At end of iteration:
    - if `required > 1`:  there's excess steps -> fail -> return `False`
    - if `required == 1`: you have enough steps -> pass -> return `True`

### Method 2: Greedy

Big Picture: jump forward as long as you have jump power remaining.

Steps:
1. Initialize `jump_power` to `0`.
2. Iterate over each `number` in `nums`, *except* the last index. You don't need to check last index, since it's the objective.
3. Set `jump_power` to the maximum of `number` and `jump_power`.  Essentially, keep the highest of current jump power, or the power available in the current index.
4. Check `jump_power`:
    - if `jump_power > 1`: decrement it by `1` and continue
    - if `jump_power == 0`: can't move any further -> return `False`
5. If you make it to last index, return `True`.

## Results (Python 3)

**Method 1**: 902 ms, 15.3 MB (24.16%, 50.29%)

**Method 2**: 614 ms, 15.1 MB (65.04%, 82.11%)
