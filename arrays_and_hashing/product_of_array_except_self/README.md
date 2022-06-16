# Product of Array Except Self ([LC238](https://leetcode.com/problems/product-of-array-except-self/))
Difficulty: **Medium**

## Problem

Given an integer array nums, return an array `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.
Constraints:
- `2 <= nums.length <= 10⁵`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

**Follow up**: Can you solve the problem in `O(1)` extra space complexity? (The output array **does not count** as extra space for space complexity analysis.)

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Can't use division
- Must have `O(n)` runtime complexity
- Negative numbers
- Handling the 1st number in `nums` (must account for it)

## Procedure

### Method 1: Forward and Reverse Pass (inc. Follow-Up)

Big Picture:
1. Gather running product of all nums to the **left** of each number in *L to R* pass.
2. Gather running product of all nums to the **right** of each number in *R to L* pass.

Steps:
1. Store `foward_product = nums[0]`, the first value in `nums`.
2. Store `answer = [nums[0]]`, the first value in `nums`.
3. Perform a *left-to-right* pass for each `num` in `nums`, starting from `nums[1]`
4. For each `num` in `nums[1:]`:
    - `push` (append) `forward_product` to `answer`
    - `forward_product *= num`
5. Perform a *right-to-left* pass, updating `answer` with the running `reverse_product` of values to the *right* of the number in `answer`.
6. Return the `answer`.

Visualization where `nums = [1,2,3,4]`:
```python
# --- Forward Pass ---
       nums = [1, 2, 3, 4]      # Start
     answer = [1]               # FWD pass: nums[1] has nothing to the left of it
fwd_product = nums[1] = 1       # nums[1] will be multiplied by all to its right
       nums = [   2      ]      # Step 2
     answer = [1  1      ]      # - answer[1] = fwd_product 
                  ^
fwd_product = 2                 # - fwd_product *= nums[1]
       nums = [      3   ]      # Step 3
     answer = [1  1  2   ]      # - answer[2] = fwd_product 
                     ^
fwd_product = 6                 # - fwd_product *= nums[2]
       nums = [         4]      # Step 4
     answer = [1  1  2  6]      # - answer[3] = fwd_product 
                        ^  
fwd_product = 24                # - fwd_product *= nums[3]

# --- Reverse Pass ---
rev_product = 1                 # - starting at 1 (effectively empty)
       nums = [         4]      # Step 5
     answer = [1  1  2  6]      # - answer[3] = rev_product 
                        ^   
rev_product = 4                 # - rev_product *= nums[3]
       nums = [      3   ]      # Step 6
     answer = [1  1  8  6]      # - answer[2] = rev_product 
                     ^
rev_product = 12                # - rev_product *= nums[2]
       nums = [   2      ]      # Step 7
     answer = [1 12  8  6]      # - answer[1] = rev_product 
                 ^
rev_product = 24                # - rev_product *= nums[1]
       nums = [ 1        ]      # Step 8
     answer = [24 12 8  6]      # - answer[0] = rev_product
                ^
return answer: [24,12,8,6]
```

Complexity:
- Time: two passes over `n` values -> `O(n)`
- Space: no extra space needed -> `O(1)`

## Results (Python 3)

**Method 1**: 413 ms, 21.6 MB (20.13%, 33.60%)
