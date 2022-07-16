# Daily Temperatures ([LC739](https://leetcode.com/problems/daily-temperatures/))
Difficulty: **Medium**

## Problem

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a *warmer temperature*. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

Constraints:
- `1 <= temperatures.length <= 10⁵`
- `30 <= temperatures[i] <= 100`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- `len(temperatures) == 1`: return `[0]`
- "Sawtooth" pattern: e.g. `100, 90, 80, 70, 60, 50, 40, 30, 100, 90, 80, 70, 60, ...`
- Same/recurring temperatures

## Procedure

### Method 1: Reverse Iteration Dynamic Programming

Big Picture:
1. Start with `answer` filled with zeroes
2. Iterate in reverse from the back of `temperatures` and get current `temp`
3. Check the temperature of the next day `temp_next` (if present)
    - if `temp_next > temp`, set `answer` at given index to `1`
    - if `temp_next < temp`, follow the `answer` for that day repeatedly until:
        1. a higher temp is found, or
        2. the `answer` for that day is `0` (no higher temperatures after this one)
    - if no higher temps are found, set current `answer` to zero

Complexity:
- Time: `O(2n)` -> `O(n)` (???)
- Space: no extra space aside from answer -> `O(1)`

### Failed Method: Reverse Iteration Two Pointer Sliding Window

*Note*: this gets the right answers, but is too inefficient.

Failed on Time Limit Exceeded.  The case:
> [34,34,47,47,34,34,34,47,47,47,34,47, ... 34,34,34,47,47,47]

This approach struggles when it has to look back (up to `100-30 = 70` times) to find the next highest value.

Visualization of a bad case:
```python
        40  40          40  40              40  40  40      40
    30          30  30          30  30  30              30
```
Complexity:
- Time: `O(n²)`
- Space: `O(1)`

## Results (Python 3)

**Method 1**:  1507 ms, 26.1 MB (71.43%, 6.16%)
