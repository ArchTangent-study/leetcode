# Meeting Rooms II ([LC253](https://www.lintcode.com/problem/919/))
Difficulty: **Medium**

*Note*: this is a LeetCode premium question, also available via `LintCode` problem `919`.

## Problem

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`, find *the minimum number of conference rooms required*.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- No meetings: return `0`
- One meeting: return `1`
- Mutually conflicting meetings:  in order for an extra meeting room to be needed, the meetings must be *mutually conflicting*:  if meeting A is blocked by B and C, but C doesn't block B, you only need `2` meeting rooms, not `3`.
- If a meeting ends at `10` and another starts at `10`, there is no conflict.

Key Ideas:
- Meetings conflict with themselves:  a single meeting requires 1 meeting room.

## Procedure

### Method 1: Start/End Counter (Boolean)

Remember, the number of rooms needed is the *maximum* number of *mutually* conflicting meetings.

Steps:
1. Gather (`time`, `is_start`) (`int`, `bool`) tuple pairs in a list.
2. Sort the list (by *lowest* time).
3. Create `count` and `max_count` variables.
4. Iterate over the list of tuple pairs.
5. If the pair is a `start` value, increment `count`.
6. If the pair is an `end` value, set `max_count`, *then* decrement `count`.
7. Return the `max_count`.

Complexity:
- Time: `O(n log n)` due to quicksort
- Space: an `int` and `bool` for each interval -> `O(n)`

Example 1: `intervals = [(0,30), (5,10), (15,20)]`

```
        [-----------------------------------]
              [-----]
                          [-----]
        
time    0     5    10    15    20    25    30
```
```python
times = [(0, True), (5, True), (10, False), (15, True), (20, False), (30, False)]

times[0]: is_start == True; count += 1
times[1]: is_start == True; count += 1
times[2]: is_start == False; max_count = 2; count -= 1
times[3]: is_start == True; count += 1
times[4]: is_start == False; max_count = 2; count -= 1
times[5]: is_start == False; max_count = 2; count -= 1

return max_count: 2
```

Thoughts: this one was particularly tricky.  I tried a stack-based approach that worked on all of my tests, but failed on LintCode.

### Method 2: Start/End Counter (Direct)

Same as above, but with small changes:
- Instead of storing `(int, bool)` pairs in `times`, store `(int, int)` pairs of `(time, count_mod)` data.
- Directly modify `count` value by `count_mod` instead of checking if the value `is_start`.

*Note*: this only works because the sorting algorithm places the `end` values *before* the `start` values for the same values of `time`.

These small changes made a **huge** difference in performance:  this way is **~5x faster** than method 1, and was faster than **99%** of other submissions.

Example 2: `intervals = [(0,10), (10,20), (20,30)]`

```
        [-----------]
                    [-----------]
                                [-----------]
        
time    0     5    10    15    20    25    30
```
```python
times = [(0, 1), (10, -1), (10, 1), (20, -1), (20, 1), (30, -1)]

times[0]: time = 0; count = 1; max_count = 1
times[1]: time = 10; count = 0; max_count = 1
times[2]: time = 10; count = 1; max_count = 1
times[3]: time = 20; count = 0; max_count = 1
times[4]: time = 20; count = 1; max_count = 1
times[5]: time = 30; count = 0; max_count = 1

return max_count: 1
```

## Results (Python 3)

**Method 1**: 409 ms, 12.89MB (2.20%) at *LintCode*

**Method 2**: 81 ms, 6.00MB (**99.20%**) at *LintCode*
