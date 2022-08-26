# Find Median from Data Stream ([LC295](https://leetcode.com/problems/find-median-from-data-stream/))
Difficulty: **Hard**

## Problem

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.
- For example, for `arr = [2,3,4]`, the median is `3`.
- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the `MedianFinder` class:
- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

Constraints:
- `-10⁵ <= num <= 10⁵`
- There will be at least one element in the data structure before calling `findMedian`.
- At most `5 * 10⁴` calls will be made to `addNum` and `findMedian`.

Follow up:
- If all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?
- If `99%` of all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?

## Thought Process

Edge Cases / Caveats / Pitfalls:
- `get_median()` called on empty list -> N/A as per constraints
- accounting for even/odd lists
- maintaining sorted order of list with new numbers added
- getting middle number(s) when using a heap

## Procedure

### Method 1

## Results (Python 3)

**Method 1**:  ms, MB (%, %)
