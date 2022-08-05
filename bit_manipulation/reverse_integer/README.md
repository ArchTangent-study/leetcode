# Reverse Integer ([LC007](https://leetcode.com/problems/reverse-integer/))
Difficulty: **Medium**

## Problem

Given a signed 32-bit integer `x`, return `x` with its *digits reversed*. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2³¹, 2³¹ - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned)**.

Constraints:
- `-2³¹ <= x <= 2³¹ - 1`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Leading zeroes when reversing
- Numbers outside of signed 32-bit integer range
- Python's approach to integer division w/negative numbers

## Procedure

### Method 1: Digit Extraction and Reversal

*Note*: Python does integer division differently than Rust.  In Python, `-123 % 10 = -7`, but in Rust, `-123 % 10 = -3`.

*Note*: Python's integers are of variable length.

Big Picture:
1. Extract lowest digits of `x` by using `x % 10`
2. Divide `x` by `10`, shifting `x` to the right by a digit
3. Add the `digit` to a stack of `digits`.
4. Repeat steps `1` to `3` while `x != 0`.
5. Iterate in reverse over each `digit` in `digits`, tracking the power of ten `i` for each
6. Multiply `digit` by `10 ** i` and add to `answer`
7. If `answer` is > `i32::MAX` or < `i32::MIN1`, return `0`.  Otherwise, return `answer`

Visualization
```Python
x = 123

Build Digits
[3]         
[3,2]       
[3,2,1]     

Reverse iterate + build answer

digits  i digit  answer
[    1] 0    1      1        
[  2  ] 1   20     21        
[3    ] 2  300    321

return 321
```

Complexity:
- Time: traverse at most `32` digits -> `O(1)`
- Space: store at most `32` digits -> `O(1)`

### Method 2: Digit Extraction and Reversal w/Overflow Margin

Key Idea: works like *Method 1*, but uses ***margin to overflow***.  This meets the question requirement of pretending that you can't use 64-bit integers (as you can in Python).  This approach also removes the need to use a stack.

## Results (Python 3)

**Method 1**:  60 ms, 13.8 MB (29.18%, **97.20%**)

**Method 2**:  63 ms, 13.9 MB (22.21%, 63.35%)
