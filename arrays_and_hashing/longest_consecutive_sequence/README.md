# Longest Consecutive Sequence ([LC128](https://leetcode.com/problems/longest-consecutive-sequence/))
Difficulty: **Medium**

## Problem

Given an ***unsorted*** array of integers `nums`, return *the length of the longest consecutive elements sequence*.

You must write an algorithm that runs in `O(n)` time.

Constraints:
- `0 <= nums.length <= 10⁵`
- `-10⁹ <= nums[i] <= 10⁹`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Empty `nums`: return 0
- `nums` is unsorted.
- Must run in `O(n)` time.
- numbers that are spaced apart by 2, e.g. `[5, 3, 1, 7]`
- duplicate numbers in `nums`

## Procedure

### Method 1: High/Low Hashmaps

I found this problem to be *quite* difficult.  On several occasions I was able to get solutions that worked for *most* cases, and one solution that worked for all cases, but exceeded the time limit (time complexity `O(n²)`).

Here's what did work:
> store the current *lowest* and *highest* contiguous values for every number in `nums`.

Steps:
1. Store a value for longest contiguous sequence `answer = 0`.
2. Track lowest contiguous low in one map (`low_map`)
3. Track highest contiguous high in another map (`high_map`)
4. For each `number`, get lowest contiguous `low` and highest contiguous `high`:
    - `low = low_map[number - 1] if number - 1 in low_map, else number`
    - `high = high_map[number + 1] if number + 1 in high_map, else number`
5. For same `number`, update low and high map:
    - `low_map[number] = low`
    - `low_map[high] = low`
    - `high_map[number] = high`
    - `high_map[low] = high`
6. For same `number`, calculate `span = (high - low) + 1` and update `answer` if `span` is higher than `answer`.
7. Return `answer`.

Complexity:
- Time: multiple constant time operations per number in input -> `O(n)`
- Space: two maps, storing each number in input -> `O(n)`

*Note*: this can be done using a single map of `{number: [low, high]}` data, but using two maps is what first came to mind.  See the `_alt` version for an example.

### Method 2: Left-to-Right Set Deduplication

This way has two advantages:
- Requires only one data structure
- Works in one direction (left to right) vice two (number to low, number to high)

Steps:
1. Gather numbers into a set `number_set` to deduplicate
2. Iterate over each `number` in `nums`
3. If `number` starts a sequence (nothing to its left), seek to the right (`+1` increments) for contiguous values in `number_set` until the end of sequence is found.
    - remove any contiguous values from `number_set`
4. Update `answer` with the highest `span` count among all sequences

Complexity:
- Time: one traversal to build set, another to count sequence -> `O(n)`
- Space: one set storing each number in input -> `O(n)`

## Results (Python 3)

**Method 1**: 695 ms, 35.7 MB (44.91%, 6.51%)

**Method 2**: 512 ms, 28.6 MB (57.86%, 36.35%)
