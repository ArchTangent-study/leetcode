# Multiply Strings ([LC043](https://leetcode.com/problems/multiply-strings/))
Difficulty: **Medium**

## Problem

Given two *non-negative* integers `num1` and `num2` represented as *strings*, return the *product* of `num1` and `num2`, also represented as a *string*.

**Note**: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Constraints:
- `1 <= num1.length`, `num2.length <= 200`
- `num1` and `num2` consist of digits only.
- Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Can't convert inputs to integers directly
- Carrying
- Conversion back to string (left zeroes)
- `num1` and/or `num2` equal to zero

## Procedure

### Method 1: Digital Product Addition with Digit Shift

*Note*: this answers the question as per the requirements without having to use a separate array to store each digit.

Key Ideas:
- it's effectively multiplying by hand.  To visualize it, do the problem by-hand.  Then, encode the steps you have visualized.
- the `digit_shift` is the "power multiplier", and represents the power (`base 10`) of the combined digits being multiplied.  For example, `tenths place * tenths place = hundredths place`, or `10 * 10 == 100`

Visualization
```Python
num1 = 123 ; num2 = 456 ; shift = 10 ** (ix1 + ix2)

  d1 d2 ix1 ix2 shift product answer
   3  6   0   0     0      18     18
   3  5   0   1    10     150    168
   3  4   0   2   100    1200   1368 
   2  6   1   0    10     120   1488
   2  5   1   1   100    1000   2488
   2  4   1   2  1000    8000  10488
   1  6   2   0   100     600  11088     
   1  5   2   1  1000    5000  16088
   1  4   2   2 10000   40000  56088

return "56088"
```

Complexity:
- Time: multiply `m` digits by `n` digits -> `O(m * n)`
- Space: just store the digits and convert to string -> `O(1)`

Where:
- `m` is length of `num1`
- `n` is length of `num2`

## Results (Python 3)

**Method 1**: 337 ms, 13.7 MB (13.50%, **98.26%**)
