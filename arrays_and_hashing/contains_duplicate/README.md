# Contains Duplicate ([LC217](https://leetcode.com/problems/contains-duplicate/))
Difficulty: **Easy**

## Problem
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

Constraints:
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Procedure

### Method 1: defaultdict

For those experienced with Python, the standard library's `collections.defaultdict` [[LINK](https://docs.python.org/3/library/collections.html#collections.defaultdict)] is an elegant choice for this problem.  A `defaultdict(int)` object is a dictionary that assigns a default value (`0` in this case) for any key newly added to it.

The process:
1. create an empty `defaultdict(int)` as a `counter`
2. iterate over all numbers
3. if there's already 1 of that number in the `counter`, the value appears at least twice -> return `True`.  Otherwise, increment the number's count by 1.
4. if the early exit in step 3 is not triggered, no value appears twice -> return `False`

## Results (Python 3)

**Method 1**:  483 ms, 26.0 MB (78.65%, 72.88%)
