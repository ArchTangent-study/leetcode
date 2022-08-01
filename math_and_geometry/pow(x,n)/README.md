# Pow(x, n) ([LC050](https://leetcode.com/problems/powx-n/))
Difficulty: **Medium**

## Problem

Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`).

Constraints:
- `-100.0 < x < 100.0`
- `-2³¹ <= n <= 2³¹-1`
- `-10⁴ <= xn <= 10⁴`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- divide by zero (`0.0 ** -3`)
- very large exponents (allowed up to `2³¹-1`)
- Negative numbers
- Floating point accuracy

Thoughts:
- since large exponents are allowed, limiting factor will probably be ***time complexity***.
- look for special cases where calculation can be sped up, e.g. powers of `2`
- since function takes `float` input, there's likely a trick using the components of floating-point numbers (`sign`, `exponent`, `significand`)

## Procedure

### Method 1: Divide and Conquer w/Recursion

Key Idea: break up the power calculation into **two parts**, accounting for odd exponents.  Once the calculation is completed, account for negative exponents by inverting the result.

Complexity:
- Time: repeatedly cut solution in half -> `O(log n)`
- Space:  recursive depth is base 2 log  of exponent (`log₂n`)  -> `O(log n)`

### Failed Method: Divide and Conquer w/Recursion

Saved as it provides a useful lesson.  It *attempted* to use the Divide and Conquer method, but failed on TLE because it *didn't actually divide* the problem.  Take a look at the `pow(x,n)_slow.py` file to see why.

## Results (Python 3)

**Method 1**:   ms,  MB (%, %)
