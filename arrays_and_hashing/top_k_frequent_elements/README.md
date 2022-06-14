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

### Method 1: Hashmap Counter w/Sorting

Big Picture:
1. Count the occurrences of each `num` in `nums` using a dictionary.
    - a `collections.defaultdict(int)` would also work
2. Collect all all `(num, count)` pairs in a list and sort them by their `count` in *descending* order.
3. Return the top `k` `num`s in the list.

Complexity:
- Time: quicksort numbers by their count -> `O(n log n)`
- Space: store up to `n` numbers in dict -> `O(n)`

### Method 2: Hashmap Highest Count Backtrack (Follow-Up)

This is a Follow-Up question requiring *better* than `O(n log n)` time complexity.

To do that, we'll need to avoid sorting.  Thankfully, there is a way!

Big Picture:
1. Store two dictionaries: `k_tracker` which maps `count` to the `num`s with that count, and `counter`, which maps each `num` to its `count`.  
    - a `collections.defaultdict(int)` would work for `counter`
    - a `collections.defaultdict(list)` would work for `k_tracker`
2. For each `num` in `nums`, update `k_tracker` and `counter`.
3. Get the `highest_count` by finding highest `count` in `counter`.
4. Starting from `highest_count`, add each `num` from `k_tracker` to a set `top_k`, and count `highest_count` down.
5. Continue until `len(top_k) == k`
6. Return the values in `top_k` as a `list`.

Visualization for `nums = [1,2,2,3,3,3]; k = 2`
```python
k_tracker = { 1: [1, 2, 3], 2: [1, 2], 3: [3] }
counter = { 1: 1, 2: 2, 3: 3 }
highest_ count = 3
top_k: { 2, 3 }
```

Complexity:
- Time: traverse each number in `nums` once, then top `k` -> `O(n)`
- Space: store up to `n` numbers in dicts -> `O(n)`

### Method 3: Hashmap Highest Count Backtrack using DefaultDict (Follow-Up)

This is the same as Method 2, but using a `collections.defaultdict` for conciseness.

## Results (Python 3)

**Method 1**: 112 ms, 18.8 MB (**82.79%**, 32.52%)

**Method 2**: 150 ms, 18.7 MB (45.96%, 69.21%)

**Method 3*: 162 ms, 18.6 MB (37.33%, **90.77%**)
