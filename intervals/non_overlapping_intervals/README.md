# Non-Overlapping Intervals ([LC435](https://leetcode.com/problems/non-overlapping-intervals/))
Difficulty: **Medium**

## Problem

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return *the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping*.

Constraints:
- `1 <= intervals.length <= 10⁵`
- `intervals[i].length == 2`
- `-5 * 10⁴ <= start_i < end_i <= 5 * 10⁴`

## Thought Process

Questions:
- Are intervals sorted?  Does not appear as they are per constraints.
- What constitutes an overlapping interval?  Per the examples, intervals don't overlap if `current.end == next.start` .

Edge Cases / Caveats / Pitfalls:
- Empty `intervals`: N/A as per constraints
- Single interval in `intervals`: return `0`
- No overlaps: return `0`
- Multiple overlaps
- Intervals with same `start` or `end` time

## Procedure

### Method 1: Greedy Removal

Example
```
0 [---]
1   [---]
2     [---]
3       [---]
4         [---]
  0123456789012
```
`answer = 2` (remove intervals`1` and `3`)

Process:
- `running_end` starts at minimum value (`-50000` as per constraints)
- Interval `0` and `running_end` don't overlap. Set `running_end` to Interval 0's `end` of `4`
- Interval `1` and running_end overlap. Remove interval `1` since its `end` is higheer than `running_end`.  Set running end to `min(4, 6) = 4`
- Interval `2` and `running_end` don't overlap. Set `running_end` to Interval 2's `end` of `8`
- Interval `3` and running_end overlap. Remove interval `3` since its `end` is higher than `running_end`.  Set `running` end to `min(8, 10) = 8`
- Interval `4` and `running_end` don't overlap. Set `running_end` to Interval 4's `end` of `12`

Complexity:
- Time: limited by quicksort -> `O(n log n)`
- Space: store `running_end` and `answer` integers -> `O(1)`

## Results (Python 3)

**Method 1**: 2813 ms, 52.9 MB (7.45%, 22.62%)
