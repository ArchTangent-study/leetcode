# Contains Duplicate ([LC217](https://leetcode.com/problems/contains-duplicate/))
Difficulty: **Easy**

## Problem
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

Constraints:
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Procedure

### Method 1: DefaultDict

For those experienced with Python, the standard library's `collections.defaultdict` [[LINK](https://docs.python.org/3/library/collections.html#collections.defaultdict)] is an elegant choice for this problem.  A `defaultdict(int)` object is a dictionary that assigns a default value (`0` in this case) for any key newly added to it.

The process:
1. Create an empty `defaultdict(int)` as a `counter`.
2. Iterate over all numbers.
3. If there's already 1 of that number in the `counter`, the value appears at least twice -> return `True`.  Otherwise, increment the number's count by 1.
4. If the early exit in step 3 is not triggered, no value appears twice -> return `False`.

### Method 2: Sorting

A simple and succinct method that requires only the given data structure.

1. Sort the list in place.
2. Store a value (`previous`) to detect against current number in list.
3. Iterate over number list and check if current number `current` is equal to `previous`. If so, the list contains a duplicate -> return `True`.
4. If entire list is traversed without finding a duplicate, return `False`.

## Results (Python 3)

**Method 1**:  483 ms, 26.0 MB (78.65%, 72.88%)

**Method 2**:  530 ms, 26.1 MB (58.81%, 31.11%)
