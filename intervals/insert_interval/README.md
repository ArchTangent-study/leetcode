# Insert Interval ([LC057](https://leetcode.com/problems/insert-interval/))
Difficulty: **Medium**

## Problem

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the `ith` interval and `intervals` is sorted in **ascending order** by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` *after the insertion*.

Constraints:
- `0 <= intervals.length <= 10⁴`
- `intervals[i].length == 2`
- `0 <= start_i <= endi <= 10⁵`
- `intervals is sorted by start_i in ascending order.`
- `newInterval.length == 2`
- `0 <= start <= end <= 10⁵`

## Thought Process

Questions:
- Do you want the original `intervals` list to be returned (mutated in-place)?  The question seems to be worded that way.
- What constitutes an overlapping interval?  An interval *starting* at `2` will overlap with another interval *ending* at `2`.

Edge Cases / Caveats / Pitfalls:
- Empty `intervals`
- No overlaps at all: still need to insert `newInterval`
- Multiple intervals overlapping: need to possibly extend into next interval, not just current.  Idea:  keep track of `current` and `next` interval to be sure.
- `newInterval` starts before any interval in `intervals`:  can simply end and return the original `intervals`
- `newInterval` ends after any interval in `intervals`:  can simply end and return the original `intervals`

## Visualization

This problem is much easier to understand when you visualize all of the edge cases:

Edge Case 1: Completely overlapping
```
newInterval [----------------]

intervals:    [---]
                    [----]

result      [----------------]
```

Edge Case 2:  Multiple overlap
```
newInterval    [---------]

intervals:  [---]
                        [----]

result      [----------------]
```

Edge Case 3:  No overlap - `newInterval` to the left of `intervals`
```
newInterval [----]

intervals:         [---]
                        [----]

result      [----] [---][----]
```

Edge Case 4: No overlap - `newInterval` to the right of `intervals`
```
newInterval             [----]

intervals:  [---]
                 [----]

result      [---][----] [----]
```

Edge Case 5: No overlap - `newInterval` in between `intervals`
```
newInterval       [--]

intervals:  [---]
                       [----]

result      [---] [--] [----]
```

## Procedure

### Method 1: Left/Right Merge

Big Picture:
1. Gather non-overlapping intervals that are left of `newInterval` in a `left` list
2. Gather non-overlapping intervals that are right of `newInterval` in a `right` list
3. Merge overlapping intervals into `newInterval`:
    - `newInterval` start is the lowest of its own start and that of `current` interval
    - `newInterval` end is the highest of its own end and that of `current` interval
4. Combine `left`, `newInterval`, `right` as one list and return

Complexity:
- Time: traverse the list of intervals once: `O(n)`
- Space: separate lists to hold as most N intervals: `O(n)`

*Note*: this method does not update `intervals` in-place.

## Results (Python 3)

**Method 1**:  90 ms, 17.5 MB (75%, 15%)
