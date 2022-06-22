# Jump Game II ([LC045](https://leetcode.com/problems/jump-game-ii/))
Difficulty: **Medium**

## Thought Process

Edge Cases / Caveats / Pitfalls:
- indexes with `0`: can't progress
- length of `nums` is `1`: no jumps required
- finding an index that allows a finish sooner than current jump

## Visualization

```
    ------|         jump 1
      --|
        ----|       jump 2
            ----|   jump 3
              --|
    3 1 2 0 2 1 6   nums
    0 1 2 3 4 5 6   ix
```
For this case, the total number of `jumps` required is `3`.

Notes:
- jump at index `[0]` `(3)` can't get over the `0`, and needs reserve jump at index `[2]`
- jump at index `[4]` `(2)` allows for jumping to the finish before reaching index `[5]`

## Procedure

### Method 1: Greedy Reserve

Big Picture: keep track of *current* jump length and *highest available* jump length, and switching to highest available when current jump lenght is exhausted.

Steps:
1. Track `current` jump power, `reserve` jump power, and `distance` to target.
    - all decremnt by `1` for each index in `nums`.
2. Track `jumps`, the number of jumps needed to reach target.
3. Iterate over every `number` in `nums`.
4. Set `reserve` equal to highest of `reserve` and `number`.
5. If `current` jump is enough to finish, return `jumps`. If `reserve` jump is enough to finish, return `jumps + 1`.
6. If `current` jump is exhausted (`0`), increment `jumps` and use set `current = reserve`.
    - this is effectively going back to the point of the highest previous jump.
7. Since contraints require a valid answer, return an `error` if no answer if found.

Complexity:
- Time: one traversal of all `number`s in `nums` -> `O(n)`
- Space: constant extra space -> `O(1)`

## Results (Python 3)

**Method 1**: 241 ms, 15 MB (47.23%, 58.64%)
