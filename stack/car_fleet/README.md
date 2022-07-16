# Car Fleet ([LC853](https://leetcode.com/problems/car-fleet/))
Difficulty: **Medium**

## Problem

There are n cars going to the same destination along a one-lane road. The destination is `target` miles away.

You are given two integer array `position` and `speed`, both of length `n`, where `position[i]` is the position of the `ith` car and `speed[i]` is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper **at the same speed.** The faster car will **slow down** to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the *same position*).

A **car fleet** is some *non-empty* set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the ***number of car fleets*** that will arrive at the destination.

Constraints:
- `n == position.length == speed.length`
- `1 <= n <= 10⁵`
- `0 < target <= 10⁶`
- `0 <= position[i] < target`
- All the values of `position` are **unique**.
- `0 < speed[i] <= 10⁶`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Multi-layered stacking: car 2 catches up to car 1 and slows down, and after the slowdown, car 3 catches up to cars 1 and 2.
- One car: only one fleet
- Division: use floating point vs integer division for time calculations

Rules:
- There's only one lane on the road
- Cars can't pass each other

## Procedure

### Method 1: Sorted Stack

Key Idea: handle the *frontmost* fleets *first*.  This is done by combining data into a *sorted stack*.

Visualization:
```Python
target = 1 ; position = [10,8,0,5,3] ; speed = [2,4,1,1,3]

                0  1  2  3  4  5  6  7  8  9  10 11 12   pos
car 0, speed 1                                C=>        
car 1, speed 3                          C=======>        
car 2, speed 1  C=>        
car 3, speed 1                 C=>        
car 4, speed 3           C=======>        
               
Collisions:
- cars 0 & 1
- cars 3 & 4

No Collisions:
- car 2

return 3    
```

Big Picture:
1. Gather tuple of `(pos, spd)` data in a `cars` stack.
2. Sort `cars` from lowest to highest `pos`, leaving car closest to `target` at top.
3. Pop topmost `(pos, spd)` data from stack and increment `answer` by `1` (new fleet).
4. Get topmost remaining `car`s in `cars`, and check if `car` will reach `target` *before* `current` (lead) fleet
    - if so, add `car` to `current` fleet by `pop()`ing it from `cars`. Do *not* increment answer (no new fleet)
    - if not, this go back to step `3`
5. Once all `cars` exhausted, return `answer`.

Complexity:
- Time: quicksort, then traverse entire `stack` -> `O(n + n log n)` -> `O(n log n)`
- Space: stack to hold rearranged input data -> `O(n)`

## Results (Python 3)

**Method 1**: 1689 ms, 36.9 MB (28.83%, 22.22%)
