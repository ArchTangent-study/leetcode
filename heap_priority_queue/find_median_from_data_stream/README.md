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

### Method 1: Split Max/Min Heap

Key Idea: split data into lower (max heap) and upper (min heap) heaps, and always keep their lengths within 1 of each other.

Big Picture:
1.) Create a `lower` max heap for lower half of data stream
2.) Create an `upper` min heap for upper half of data stream
3.) Track even/odd status with an `even` boolean
4.) When adding a new number, add to `upper` if `number` is > lowest value in `upper`. Otherwise, add it to `lower`.
6.) Always keep lengths of `lower` and `upper` within 1 of each other.
    - if `len(lower) - len(upper) > 1`:  `heappop(lower)`, then `heappush` it onto `upper`
    - if `len(upper) - len(lower) > 1`:  `heappop(upper)`, then `heappush` it onto `lower`
        - be sure to account for *negative* values in a Python max heap
7.) get median for `even` count:
    - average highest of `lower` (max heap) with lowest of `upper` (min heap)
8.) get median for `odd` count:
    - if `len(lower) > len(upper)`, return highest value of `lower`
    - if `len(upper) > len(lower)`, return lowest value of `upper`

Complexity:
- Add Num: heappush up to `n` values with a possible added heap pop and push -> `O(n log h)`
- Find Median: constant time -> `O(1)`
- Space: `O(n)`

Where:
- `n` is the amount of numbers added to the `MedianFinder`
- `h` is the size of each `heap` (length of both will always be within 1 of each other)

### Failed Method: Single Binary Heap with Pop and Replace

This failed on "Time Limit Exceeded", but serves as a good foundation for improvement in *Method 1*.  See `_slow.py` file.

Big Picture:
1. track `even/odd` status of the `heap`
2. add new numbers with `heappush()`
3. get median for `even` `heap` by:
    - adding the first `len(nums) / 2 + 1` numbers to a `temp` list
    - averaging the the top two values in `temp`
4. get median for `odd` `heap` by:
    - adding the first `len(nums) / 2 + 1` numbers to a `temp` list
    - taking the last (highest) value in `temp`
  - return all values from temp back to the heap

## Results (Python 3)

**Method 1**: 664 ms, 33.5 MB (77.47%, **92.86%**)
