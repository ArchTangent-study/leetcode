# Merge Intervals ([LC056](https://leetcode.com/problems/merge-intervals/))
Difficulty: **Medium**

## Problem

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

Constraints:
- `1 <= intervals.length <= 10⁴`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10⁴`

## Thought Process

Questions:
- Are the intervals sorted?  Contraints don't indicate that they are.

Edge Cases / Caveats / Pitfalls:
- empty `intervals`: N/A per constraints
- `len(intervals) == 1`: simply return `intervals` (no change)
- multiple overlaps: an interval may possibly overlap more than one other interval
- no overlaps: return `intervals` with no change

## Procedure

### Method 1: Running Interval

Key Ideas:
1. Keep track of a `running` merged interval, equal to either:
    - the `current` interval in `intervals`, or
    - the largest overlapping interval found so far
2. At the start, set `running` equal to `intervals[0]`.  
    - constraints mandate at least one value in `intervals`
    - the first case will always overlap (with itself).

Steps:
1. Store a separate `merged` list to hold the merged answer.
2. Sort the `intervals` by ascending `start` order.
3. Store a `running` interval equal to the first value in `intervals`.
4. Iterate over `intervals`, performing steps `5` to `7`.
5. Compare the `running` interval vs the `current` interval in `intervals`.
6. If `running` does *not* overlap `current`, add the `running` value to `merged`, *then* set `running` equal to `current`.
7. If `running` *does* overlap `current`, merge `current` into `running` interval:
    - `running[0] = min(running[0], current[0])`
    - `running[1] = max(running[1], current[1])`
8. At end of iteration, append the `running` interval to `merged`.
9. Return the `merged` intervals.

Complexity:
- Time: `O(n log n)` due to quicksort of input
- Space: `O(n)` to store

## Results (Python 3)

**Method 1**: 219 ms, 18.1 MB (37.41%, 51.16%)
