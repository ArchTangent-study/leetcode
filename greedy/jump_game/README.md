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

## Results (Python 3)

**Method 1**: 902 ms, 15.3 MB (24.16%, 50.29%)
