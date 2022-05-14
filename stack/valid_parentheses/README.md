# Valid Parentheses ([LC020](https://leetcode.com/problems/valid-parentheses/))
Difficulty: **Easy**

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Constraints:
- `1 <= s.length <= 10⁴`
- `s` consists of parentheses only `'()[]{}'`.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Two of the same opening brackets before a closing bracket (e.g. two `(`s before a `)`)
- Two of the same closing brackets before an opening bracket (e.g. two `]]`s  before a `[)`)
- Encloding a different opening bracket: `"([)]"` is invalid while `"{[]}"` is valid
- Unbalanced brackets: number of matched closing brackets `!=` number of opening ones
- Unclosed brackets (e.g. `(` without a `)`) at the end of the string

Approaches:
1. Use *toggling*: track the current bracket status (`open` or `closed`) for each of the three bracket types, checking for invalid conditions after:
    - each new bracket is added
    - at end of input, to make sure all brackets are `closed`
2. Use a *stack*: as you add parentheses to the stack, ensure the state is valid and early exit with `False` if it isn't.

## Procedure

### Method 1: Stack and Track

Key Rules:
- Can't start with a closing bracket.
- Can't end with an opening bracket.
- Can't add a closing bracket to an empty `bracket` list (must have an opening present).
- Closing brackets can't enclose an open (unclosed) mismatched bracket.
- The number of opening parentheses of a given type must equal that of its matching closing parentheses.

Algorithm:
1. Add first `char` in input `s` to an empty `brackets` list (guaranteed as `len(s) >= 1`):
    - if `char` is a closing bracket, return `false`
    - if `char` is an opening bracket, add it to `brackets`
2. Iterate over remaining `char`s in `s` (from `[1:]`)
    - if `char` is an opening bracket, add it to `brackets`
    - if `char` is a closing bracket: check the last value in `brackets`:
        - if it is *not* an opening bracket that matches the closing bracket: return `false`
        - if it *is* the matching opening bracket, `pop` it from `brackets`
3. At end of the input `s`, check length of `brackets`:
    - if `len = 0`, return `true` - the input was valid
    - if `len != 0`, return `false` - the input was invalid

Visualization 1 (Valid):
```
s = '{[]}'
        char    brackets    
step 1  '{'     ['{']           s[0] is an opening bracket -> add to brackets
step 2  '['     ['{', '[']      '[' is an opening bracket -> add to brackets
step 3  ']'     ['{']           ']' is closing and brackets[-1] matches -> pop '['
step 4  '}'     []              '}' is closing and brackets[-1] matches -> pop '}'
finish                          brackets is empty -> return True
```

Visualization 2 (Invalid):
```
s = '([)]'
        char    brackets    
step 1  '('     ['(']           s[0] is an opening bracket -> add to brackets
step 2  '['     ['(', '[']      '[' is an opening bracket -> add to brackets
step 3  ')'     ['(', '[']      ')' is closing and brackets[-1] does NOT match -> invalid
                                return False
```

Pitfalls:
- Checking the last index in `brackets` while it's empty.  To avoid a runtime error, check if `len(brackets) > 0` first.

### Method 2: Stack and Track (Rewrite)

Same as method 1, but rewritten to better match the logical intent.

This was **~27%** faster than method 1.

## Results (Python 3)

**Method 1**:  37 ms, 13.8 MB (69.08%, 70.91%)

**Method 2**:  29 ms, 14.0 MB (98.83%, 24.86%)
