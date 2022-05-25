# Minimum Interval to Include Each Query ([LC1851](https://leetcode.com/problems/minimum-interval-to-include-each-query/))
Difficulty: **Hard**

## Problem

You are given a 2D integer array `intervals`, where `intervals[i] = [left_i, right_i]` describes the `ith` interval starting at `left_i` and ending at `right_i` **(inclusive)**. The **size** of an interval is defined as the number of integers it contains, or more formally `right_i - left_i + 1`.

You are also given an integer array `queries`. The answer to the `jth` query is the **size of the smallest interval** i such that `left_i <= queries[j] <= right_i`. If no such interval exists, the answer is `-1`.

*Return an array containing the answers to the queries*.

Constraints:
- `1 <= intervals.length <= 10⁵`
- `1 <= queries.length <= 10⁵`
- `intervals[i].length == 2`
- `1 <= lefti <= righti <= 10⁷`
- `1 <= queries[j] <= 10⁷`

## Thought Process

Edge Cases / Caveats / Pitfalls:

## Procedure

### Method 1

## Results (Python 3)

**Method 1**:  ms, MB (%, %)
