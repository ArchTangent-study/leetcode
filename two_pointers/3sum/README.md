# 3 Sum ([LC015](https://leetcode.com/problems/3sum/))
Difficulty: **Medium**

## Problem

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

**Note**: the solution set must not contain duplicate triplets.

Constraints:
- `0 <= nums.length <= 3000`
- `-10⁵ <= nums[i] <= 10⁵`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- OOB indexing
- Duplicate answers

Ideas:
- Sorting
- Backtracking
- Three Pointers (`O(n³)`)
- Binary Search
- Hashing (deduplicate identical combinations)
- If sorted, any starting value > `0` indicates no answer available

## Procedure

### Method 1: Three Pointers w/Two Pointer Closing Window, Set Deduplication, and Sorting

Key Ideas:
- Sort `O(n log n)` in advance to make subsequent calculations faster
- Deduplicate by `1st` number `L` and `2nd` number `M` once each has been fully explored
- Use techniques learned in previous "sum" problems:
    - Two Sum ([LC001](https://leetcode.com/problems/two-sum/))
    - Two Sum II ([LC167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/))

Visualization:

Where:
- `nums = [-1,0,1,2,-1,-4] ; target = 0`
- `set1` holds first numbers that have been fully explored for `L`
- `set2` holds second numbers that have been fully explored for a given `L` (each `L,M` combo)
```python

-4 -1 -1  0  1  2   set1    set2
 L  M           R                   sum = -3 < 0
 L     M        R             -1    M.val -1 in set2 ; skip
 L        M     R           -1,0    sum = -2 < 0
 L           M  R         -1,0,1    sum = -1 < 0
                      -4            M !< R ; shift L
    L  M        R     -4            sum == 0; add [-1,-1,2] to answer
    L     M     R     -4       -1   sum = 1 > 0
    L     M  R        -4       -1   sum == 0; add [-1,0,1] to answer
                   -4,-1            M !< R; shift L
       L  M     R  -4,-1            L.val -1 in set1 ; skip
          L  M  R  -4,-1            sum = 3 > 0
                                    M !< R ; shift L)
            LM  R  -4,-1            L !< len(nums) - 2 ; STOP

return [[-1,-1,2],[-1,0,1]]   
```

Complexity:
- Time: for each `L` value, traverse up to `n` numbers with `M` and `R` -> `O(n²)`
- Space: two sets with up to `n` numbers -> `O(n)`

### Method 2: Three Pointers w/Two Pointer Closing Window, Int Deduplication, and Sorting

Key Idea: same as Method 1, but uses the fact that values are sorted to deduplicate by simply checking if the first/second number is the same as it was in the previous pass.  This saves time and space.

Complexity:
- Time: for each `L` value, traverse up to `n` numbers with `M` and `R` -> `O(n²)`
- Space: constant extra space -> `O(1)`

## Results (Python 3)

**Method 1**: 1462 ms, 18.1 MB (44.71%, 72.14%)

**Method 2**: 1127 ms, 18.0 MB (63.85%, 81.75%)
