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

## Procedure

### Method 1

## Results (Python 3)

**Method 1**:   ms,  MB (%, %)