# Time Based Key-Value Store ([LC981](https://leetcode.com/problems/time-based-key-value-store/))
Difficulty: **Medium**

## Problem

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:
- `TimeMap()` Initializes the object of the data structure.
- `void set(String key, String value, int timestamp)` Stores the key key with the value value at the given time timestamp.
- `String get(String key, int timestamp)` Returns a value such that set was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

Constraints:
- `1 <= key.length`, `value.length <= 100`
- `key` and `value` consist of lowercase English letters and digits.
- `1 <= timestamp <= 10⁷`
- All the timestamps `timestamp` of `set` are *strictly increasing*.
- At most `2 * 10⁵` calls will be made to `set` and `get`.

## Thought Process

Edge Cases / Caveats / Pitfalls:

## Procedure

### Method 1

## Results (Python 3)

**Method 1**:  ms, MB ( %, %)
