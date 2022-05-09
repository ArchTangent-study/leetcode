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

Approaches:
- Sorting in a list and taking `kth` values -> sorting, in particular using a *binary heap*, is advisable.

## Procedure

### Method 1: Repeated Sorting

AKA *Smash and Sort*.  This is similar to the approach used in *Kth Largest Element in a Stream* ([LC703](https://github.com/ArchTangent-study/leetcode/tree/main/bit_manipulation/kth_largest_element_in_a_stream)).

Key Steps:
1. Sort all `stones` from lowest to highest
2. If no stones remain, return `0`
3. If only one stone remains, return the weight of that stone
4. Otherwise, "smash" two largest stones
    - if stones are same value, destroy both
    - if stones have different values:
        1. destroy smaller stone return new stone equal to (larger - smaller)
        2. sort the list of stones

### Method 2: Binary Heap with Negation

Similar to method 1, but using a *binary heap* instead of *quicksort*.  Since Python's `heapq` uses a *min heap*, you need to *negate* the weights in `stones` so that the heaviest stones will be at index `[0]`. An example:

```
stones = [1, 2, 3, 2, 3, 4, 5]         (min heap)
stones = [-5, -3, -4, -2, -2, -1, -3]  (min heap with negation)
```

Key Steps:
1. Negate all values in `stones`, making the *heavier* stone have *smaller* values
2. Convert `stones` into a binary heap (min heap)
3. If no stones remain, return `0`
4. If only one stone remains, return the weight of that stone
5. Otherwise, "smash" two largest stones (the ones with the *lowest* weight)
    - if stones are same value, destroy both
    - if stones have different values:
        1. destroy smaller stone return new stone equal to (larger - smaller)
        2. add new stone to the heap

*Note*: this method is rife with pitfalls, and can trip you up if you don't account for the fact that the original values have been negated.

## Results (Python 3)

**Method 1**:  54 ms, 13.9 MB (27.63%, 66.96%)

**Method 2**:  34 ms, 13.9 MB (81.33%, 17.29%)
