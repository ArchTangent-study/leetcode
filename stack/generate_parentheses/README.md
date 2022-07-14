# Generate Parentheses ([LC022](https://leetcode.com/problems/generate-parentheses/))
Difficulty: **Medium**

## Problem

Given `n` pairs of parentheses, write a function to generate *all combinations of well-formed parentheses*.

Constraints:
- `1 <= n <= 8`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Only rounded parens `"(" , ")"` are used

Rules:
- First paren must be open
- Last paren must be closed
- Each open must have a close
- Can't have more closed than open at any time

Thoughts:
- Whenever a question asks to "find all combinations" or something to that effect, *backtracking* is a possible solution.

## Procedure

### Method 1: Backtracking

Key Idea: branching paths - left path adds open parens; right path adds closed parens.

*Note*: since all valid parentheses start with an open parenthesis (`"("`), there's no need to start from an empty string `""`.

Visualization (`n = 2`)
```python
                (
      ((                    ()       
         (()            ()(                  
            (())            ()()      
    
result = ["(())", "()()"]
```

Complexity:
- Time: two paths for every opening *or* closing parens -> `O(2²ⁿ)` -> `O(2ⁿ)`
- Space: store temporary strings up to length `2n` -> `O(n)`

## Results (Python 3)

**Method 1**: 52 ms, 14.2 MB (57.37%, 76.81%)
