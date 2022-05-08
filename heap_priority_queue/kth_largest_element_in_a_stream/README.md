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
- Empty list: `nums` can be empty
- `nums` length less than `k`: in this case, all values added will be among `kth` largest
- Equal numbers:  be sure to handle cases where an added number is equal to one already in the list.
- Keeping vals: is it necessary to store all incoming values from the stream? Answer: *no*.

Approach 1: Repeated Sorting
- Use *sorting* at initialization to get the starting order of `nums` from low to high
- Use *sorting* after each new number is added
- Return the `kth` highest index by using `nums[-k]`

This approach is simpler to implement, but requires a quicksort every time a number is added.

Approach 2: Binary Heap
- Use a *binary heap*, which is well-suited to these problems.  For Python, this requires `heapq` from the standard library [LINK](https://docs.python.org/3/library/heapq.html).

This approach is simple and efficient if using Python.

## Procedure

### Method 1: Repeated Sorting

Key Steps:
1. sort `nums` on initialization
2. sort `nums` when `add(val)` is called
3. return `nums[-k]` from `add()`

Thoughts: as expected, this method isn't particularly fast, but it *is* simple and easy to implement.

### Method 2: Binary Heap

Use a binary heap, keeping only the largest `k` values from the stream.

This is **~9x** faster than method 1.

*Note*: Python's `heapq` uses a *min heap*.  

Key Steps:
1. On initialization, use `heapq.heapify()` to convert `nums` into a binary heap
2. Keep only the top `k` values after initialization (remove smallest via `heapq.heappop()`)
3. On `add(val)`, use `heapq.heappush()` to add `val` to binary heap
4. Keep only the top `k` values after adding a value (remove smallest via `heapq.heappop()`)
5. Get `kth` largest value by returning lowest value in the heap

Visualization where `k=3`, adding `3`, `5`, then `8`:
```
nums    [4, 3, 2, 6, 7, 5, 1]
init    [1, 3, 2, 6, 7, 5, 4]           after heapify()
        [5, 6, 7]                       keep only k highest via heappop()
add 3   [3, 5, 7, 6]                    after heappush(heap, 3)
        [5, 6, 7]                       keep only k highest via heappop()
add 5   [5, 5, 7, 6]                    after heappush(heap, 5)
        [5, 6, 7]                       keep only k highest via heappop()
add 8   [5, 6, 7, 8]                    after heappush(heap, 8)
        [6, 8, 7]                       keep only k highest via heappop()
```

Thoughts: Python's `heapq` makes this quite simple if you are aware of it.

### Method 3: Reverse Sorted List

Use a simple Python `list` that hold `k` values, sorted from lowest to highest for better performance when `pop()`ing the list.

This is **~2.5x** faster than method 1.

Key Steps:
1. sort `nums` on initialization
2. Keep only the top `k` values after initialization (remove all `length(nums) - k` smallest values from `nums`)
3. On `add(val)`:
    1. add value and sort if `len(nums) < k` *or* `val`len(nums) , k`
    2. do *not* add `val` if it is less than the smallest value in `nums`
    3. return the smallest value in `nums`

## Results (Python 3)

**Method 1**:  1185 ms, 18.3 MB (13.35%, 13.35%)

**Method 2**:  126 ms, 18.1 MB (64.25%, 88.55%)

**Method 3**:  487 ms, 18.3 MB (18.73%, 33.82%)

## Final Thoughts

A binary heap ideally suited for this sort of problem, and Python makes it easy.
