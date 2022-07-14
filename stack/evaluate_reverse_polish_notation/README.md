# Evaluate Reverse Polish Notation ([LC150](https://leetcode.com/problems/evaluate-reverse-polish-notation/))
Difficulty: **Medium**

## Problem

Evaluate the value of an arithmetic expression in [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression.

*Note*: division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is *always valid*. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Constraints:
- `1 <= tokens.length <= 10⁴`
- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- More than two integers before an operand
- Only one token, e.g. `["4"]`
- operand order: if using a stack, the 1st item `pop()`ed is the 2nd operand
- Python division types: this problem requires integer division (`//`)
- Python division w/negative numbers: `6 // -132` returns `-1` (problem requires `0`)
    - workaround: use `int(6 / -132)`
- Multiple-digit numbers: not an issue for Python, but can be for languages like C.

## Procedure

### Method 1: Stack with Match Case

Big Picture:
1. Each operator acts on two operands
2. If incoming `token` is a number, convert it to an integer and add it to stack
3. If incoming `token` is an operator, pop the top two operands
    - 1st popped is 2nd operand `op2`; 2nd popped is 1st operand `op1`
    - perform given operation on the two operands, e.g. (`op1 * op2`)
    - add result back to stack
4. After all `token`s used, return the final value left in `stack`

Complexity:
- Time:  proportional to number of `tokens` -> `O(n)`
- Space: `stack` size proportional to number of `tokens` -> `O(n)`

## Results (Python 3)

**Method 1**:  85 ms, 14.3 MB (72.46%, 56.91%)
