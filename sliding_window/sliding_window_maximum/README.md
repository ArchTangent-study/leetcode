# Sliding Window Maximum ([LC239](https://leetcode.com/problems/sliding-window-maximum/))
Difficulty: **Hard**

## Problem

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the *max sliding window*.

Constraints:
- `1 <= nums.length <= 10⁵`
- `-10⁴ <= nums[i] <= 10⁴`
- `1 <= k <= nums.length`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- OOB indexing
- Proper indexing for slices vs direct indexing
- Tracking index of maximum value within moving window
- Constantly decreasing numbers, e.g. `[8,7,6,5,4,3,2,1]`
- Window `k` larger than `nums` list -> N/A as per constraints
- Incoming number equal to current max value -> update w/index of incoming number
- Current window maximum falling out of window -> need to replace w/max currently in window

Optimizations:
- Tracking index of current maximum within window: keeps from having to check the entire window each time (until it falls out of window, at least)
- Tracking a *next highest* value, and its index: when getting the higest value in a window, track the second highest value that is to the right of the highest.  May be useful in case the current maximum falls out of the window w/no replacement.

Worst-Case Scenarios:
- Constantly-decreasing numbers
- Large windows (large `k`)

## Procedure

### Method 1: Sliding Window with (val, ix) Max Heap

Key Idea: use a `(value, index)` max heap, using the `index` of the associated `value` to see if the `value` is within the bounds of the current `p1` to `p2` window.
- If `index` is in bounds (`index >= p1`), `value` is the maximum of the window.
- If `index` is *not* in bounds (`index < p1`), remove `value` from heap and try again.

Visualization 1 (worst space case)
```Python
nums = [1,2,3,4,5,6,7,8]; k = 4; expected = [4,5,6,7,8]

window      heap        answer 
1234        4321        4
 2345       54321       45
  3456      654221      456
   4567     7654321     4567
     5678   87654321    45678

return [4,5,6,7,8]
```
Note how the heap keeps increasing in size -> `O(n)` worst case space complexity

Visualization 2 (best space case)
```Python
nums = [8,7,6,5,4,3,2,1]; k = 3; expected = [8,7,6,5,4,3]

window      heap        answer 
876         876         8
 765        765         87
  654       654         876
   543      543         8765
    432     432         87654
     321    321         876543

return [4,5,6,7,8]
```
Note how the heap stays the same size -> `O(k)` best case space complexity

Complexity:
- Time: `O(k log k)` initial heapsort, `O(log k)` heap insert for each `n` in `nums` -> `O(n log k)`
- Space: in worst case (increasing list), `heap` holds all `n` numbers -> `O(n)`

### Method 2: Sliding Window with (val, ix) Max Heap - Improved

Key Idea: improve performance and space complexity by clearing irrelevant items from the heap.  When an incoming value is the *new high* of the heap, it replaces *all other* values in the heap.  See the *Visualization* below, compared to that of Method 1.

Visualization 1
```Python
nums = [1,2,3,4,5,6,7,8]; k = 4; expected = [4,5,6,7,8]

window      heap        answer 
1234        4           4
 2345       5           45
  3456      6           456
   4567     7           4567
     5678   8           45678

return [4,5,6,7,8]
```

Caveat: when checking for equality (whether `incoming` is the highest in the heap), you need to account for the way Python sorts `tuple`s.  If you have `(-10, 0)` and `(-10, 3)` in the heap, `(-10, 0)` will be at the top of the heap since it's a *min heap* and index `0` is before `3`.  To fix this, use `heap[:] = [(-n, i)]` instead of `del(heap[1:])`

Complexity:
- Time: `O(log k)` heap insert for each `n` in `nums` -> `O(n log k)`
- Space: in worst case (decreasing list), `heap` holds `k` numbers -> `O(k)`

### Failed Method: Sliding Window w/Early Exit

*Note:* this way failed on *Time Limit Exceeded*, but actually gets the correct answer.  Stored under `sliding_window_maximum_slow.py` for reference purposes.

Advantages:
- Simple
- Constant space

Complexity:
- Time: `n - k` vals for each `n`, worst case when `k = n/2` -> `O((n-k)*k)` -> `O(k²)`
- Space: constant space -> `O(1)`

## Results (Python 3)

**Method 1**: 3562 ms, 39.6 MB (14.44%, 5.31%)

**Method 2**: 3218 ms, 35.8 MB (24.73%, 8.43%)
