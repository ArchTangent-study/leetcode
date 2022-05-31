# Meeting Rooms ([LC252](https://www.lintcode.com/problem/920/))
Difficulty: **Easy**

*Note*: this is a LeetCode premium question, also available via `LintCode` problem `920`.

## Problem

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`, determine *if a person could attend all meetings*.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Empty list of invervals
- Single interval
- Case where `Inverval.start` equals previous `Interval.end`: this is a valid case (you can make the meeting)

## Procedure

### Method 1: Sorted Intervals

Visualization
```
    A1 ----- A2

             B1 ------------ B2

                    C1 --- C2
```
Key Ideas:
- The intervals are *sorted* from low to high `start` time.
- If the `start` of an interval is greater then or equal to the `end` of the previous interval, the meeting can be attended.
- Otherwise, the meeting cannot be attended -> return `false`.
- If all intervals are checked without fail -> return `true`.

In summary, if the current meeting ends after the next one, you can't attend all meetings.

## Results (Python 3)

**Method 1**: 163 ms, 9.02 MB (54.60%) on *LintCode*
