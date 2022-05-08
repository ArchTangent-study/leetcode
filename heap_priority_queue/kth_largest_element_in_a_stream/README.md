# Kth Largest Element in a Stream ([LC703](https://leetcode.com/problems/kth-largest-element-in-a-stream/))
Difficulty: **Easy**

## Problem

Design a class to find the `kth` largest element in a stream. Note that it is the `kth` largest element in the *sorted* order, not the `kth` distinct element.

Implement `KthLargest` class:
- `KthLargest(int k, int[] nums)` Initializes the object with the integer `k` and the stream of integers `nums`.
- `int add(int val)` Appends the integer `val` to the stream and returns the element representing the `kth` largest element in the stream.

Constraints:
- `1 <= k <= 10^4`
- `0 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `-10^4 <= val <= 10^4`
- At most `10^4` calls will be made to `add`.
- It is guaranteed that there will be at least `k` elements in the array when you search for the `kth` element.

## Thought Process

Edge Cases / Pitfalls:
- Equal numbers:  be sure to handle cases where an added number is equal to one already in the list.

Approach 1: Repeated Sorting
- Use *sorting* at initialization to get the starting order of `nums` from low to high
- Use *sorting* after each new number is added
- Return the `kth` highest index by using `nums[-k]`

This approach is simpler to implement, but requires a quicksort every time a number is added.

Approach 2: Index Windows
- Use *sorting* at initialization to get the starting order of `nums` from low to high
- Track the *index* of the `kth` highest value: `kth_index`
- Track the *index* of the highest value: `high_index`
- Adjust one or more of above indexes as numbers are added, based on relation to numbers at `nums[kth_index]` and `nums[highest_index]`
- Use indexing at `kth_index` to return the `kth` highest index

This approach is tougher to implement, but only requires a single quicksort at initialization.

## Procedure

### Method 1: Repeated Sorting

Key Steps:
1. sort `nums` on initialization
2. sort `nums` when `add(val)` is called
3. return `nums[-k]` from `add()`

Thoughts: as expected, this method isn't particularly fast, but it *is* simple and easy to implement.

## Results (Python 3)

**Method 1**:  1185 ms, 18.3 MB (13.35%, 13.35%)
