# Two Sum II - Input Array is Sorted ([LC167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/))
Difficulty: **Medium**

## Problem

Given a **1-indexed** array of integers `numbers` that is already ***sorted in non-decreasing order***, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1₁` and `numbers[index₂]` where `1 <= index₁ < index₂ <= numbers.length`.

Return the indices of the two numbers, `index₁` and `index₂`, ***added by one*** as an *integer array* `[index₁, index₂]` of *length 2*.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant (`O(1)`) extra space.

Constraints:
- `2 <= numbers.length <= 3 * 10⁴`
- `-1000 <= numbers[i] <= 1000`
- numbers is sorted in **non-decreasing order**.
- `-1000 <= target <= 1000`
- The tests are generated such that there is **exactly one solution**.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Proper indexing (`1`-indexed)
- Constant space `O(1)`
- Only one answer
- Can only use each element once
- Multiples of same value, e.g. `[1,2,2,2,3]`

Ideas:
- Since values are non-decreasing, early exit can be used once a value higher than `target` is found.

## Procedure

### Method 1: Two Pointers Naive w/Early Exit

Note: this gets the right answers, but fails on Time Limit Exceeded

Key Idea: a naive (brute force) two pointers approach with early exit if the `combined` sum is greater than `target`.

Complexity:
- Time: `O(n²)`
- Space: `O(1)`

### Method 2: Binary Search

Key Idea: take advantage of the fact that `numbers` is sorted to split the effective search range for the second number in half.

Visualization

Where:
- `S` is starting index (1st number in sum)
- `L` and `R` are left/right pointers for binary search
- `M` is the midpoint of binary search and 2nd number in sum

*Note*: `S` and `L` cannot start at same index!
```python
nums = [2,3,15,20,25,30,50] ; target = 28 

 0  1  2  3  4  5  6    indices
 2  3 15 20 25 30 50    nums
 S  L     M        R    sum = 22 < 28   
 S           L  M  R    sum = 32 > 28
 S          LMR         sum = 27 < 28
 S        R  L          R < L ; move to next S
    S  L     M     R    sum = 28 = 28 *correct*
    
return [S+1, M+1] = [2,5]
```

Complexity:
- Time: binary search for each `n` in `numbers` -> `O(n log n)`
- Space: constant extra space -> `O(1)`

This performed poorly (`~5%`) in the time ranking, so certainly there's a better way!

## Results (Python 3)

**Method 1**:  Failed - Time Limit Exceeded

**Method 2**: 394 ms, 14.9 MB (5.04%, **88.35%**)
