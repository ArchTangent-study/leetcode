# Gas Station ([LC134](https://leetcode.com/problems/gas-station/))
Difficulty: **Medium**

## Problem

There are `n` gas stations along a circular route, where the amount of gas at the `ith` station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `ith `station to its next `(i + 1)th` station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return *the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return* `-1`. If there exists a solution, it is **guaranteed** to be **unique**.

Constraints:
- `n == gas.length == cost.length`
- `1 <= n <= 10⁵`
- `0 <= gas[i], cost[i] <= 10⁴`

## Thought Process

Questions:
- If there's only one station, do you still have to loop to it?  Assuming *yes*.

Key Ideas:
- One circuit means traveling `len(gas)` indexes.
- Can make iteration easier by duplicating `gas` and `cost` and appending them to the existing `gas` and `cost` lists (since all you need is one loop).

Edge Cases / Caveats / Pitfalls:
- Empty list
- Out of bounds indexing
- Looping to beginning of the track
- Mismatched `gas`/`cost` lengths (N/A as per constraints)
- Length of `gas`/`cost` being `1`
- Zero `gas` values

## Visualization

You can simulate traversal of a single loop by doubling the input lists.

So this:
```
      /-----[0]------\
    [4]             [1]     indexes
      \--[3]----[4]--/
```

Turns into this:
```
   1    2    3    4    5    1    2    3    4    5       gas
  [0]--[1]--[2]--[3]--[4]--[0]--[1]--[2]--[3]--[4]      index
   3    4    5    1    2    3    4    5    1    2       cost
```

If you traverse the entire "unrolled" list without finding a solution, you know you have done an entire loop of the track.

## Procedure

### Method 1: Greedy Doubled List Iteration

A nice trick for this one is doubling the `gas` and `cost` lists to allow for easy iteration over 1 (simulated) loop, without having to track indexes (resetting index to 0 once end is hit). This is done using `gas*2`, `cost*2` to double the lists.

Complexity:
- Time: double each list, then traverse zipped pair -> `O(n)`
- Space: twice the size of each input list -> `O(n)`

One could save space by simply using indexes over `gas` and `cost` (w/o doubling each list), but this felt simpler.

## Results (Python 3)

**Method 1**:  1077 ms, 21.4 MB (29.07%, 5.75%)
