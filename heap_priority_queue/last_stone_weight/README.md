# Last Stone Weight ([LC1046](https://leetcode.com/problems/last-stone-weight/))
Difficulty: **Easy**

## Problem

You are given an array of integers `stones` where `stones[i]` is the weight of the `ith` stone.

We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

- If `x == y`, both stones are destroyed, and
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.

At the end of the game, there is at most one stone left.

Return the *smallest possible weight of the left stone*. If there are no stones left, return `0`.

Constraints:
- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- no stones remaining -> return `0`
- one stone remaining -> return its weight

## Procedure

### Method 1: Repeated Sorting

AKA *Smash and Sort*.  This is similar to the approach used in *Kth Largest Element in a Stream* ([LC703](https://github.com/ArchTangent-study/leetcode/tree/main/bit_manipulation/kth_largest_element_in_a_stream)).

Key Steps:
1. If only no stones remain, return `0`
2. If only one stone remains, return the weight of that stone
3. Otherwise, "smash" two largest stones
    - if stones are same value, destroy both
    - if stones have different values:
        1. destroy smaller stone return new stone equal to (larger - smaller)
        2. sort the list of stones

## Results (Python 3)

**Method 1**:   ms,  MB (%, %)
