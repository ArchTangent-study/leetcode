# Top K Frequent Elements ([LC347](https://leetcode.com/problems/top-k-frequent-elements/))
Difficulty: **Medium**

## Problem

Given an integer array `nums` and an integer `k`, return the `k` *most frequent elements*. You may return the answer in **any order**.

Constraints:
- `1 <= nums.length <= 10⁵`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

**Follow up**: Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Empty list: N/A as per constraints
- Tiebreakers - what if there are multiple answers: N/A as per constraints

## Procedure

### Method 1

Big Picture:
1. Count the occurrences of each `num` in `nums` using a dictionary.
    - a `collections.defaultdict(int)` would also work
2. Collect all all `(num, count)` pairs in a list and sort them by their `count` in *descending* order.
3. Return the top `k` `num`s in the list.

Complexity:
- Time: quicksort numbers by their count -> `O(n log n)`
- Space: store up to `n` numbers in dict -> `O(n)`

## Results (Python 3)

**Method 1**: 112 ms, 18.8 MB (82.79%, 32.52%)
