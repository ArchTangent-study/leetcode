# Climbing Stairs ([LC070](https://leetcode.com/problems/climbing-stairs/))
Difficulty: **Easy**

## Problem

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

Constraints:
- `1 <= n <= 45`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- `n < 1`: N/A as per constraints

Key Idea: the number of step combinations for `number` is equal to sum of those of `number - 1` and `number - 2` combined.

## Procedure

### Method 1: List Cache

Examples:
- The # of unique combinations for `3` is equal to those of `2` plus those of `1`.
- The # of unique combinations for `4` is equal to those of `3` plus those of `2`.
- The # of unique combinations for `5` is equal to those of `4` plus those of `3`.

This can be converted into an algorithm, using a hashmap that *caches* the previous values.

Complexity:
- Time: traverse each number from `1` to `n` once -> `O(n)`
- Space: store one number from `1` to `n` -> `O(n)`

### Method 2: Hash Cache

Similar to method 1, but using a hashmap instead.

Complexity:
- Time: traverse each number from `1` to `n` once -> `O(n)`
- Space: store one number from `1` to `n` -> `O(n)`

### Method 3: Iterative Sum

Visualization:
```
n     | 3   4   5   6   
------|--------------
num-1 | 2   3   5   8
num-2 | 1   2   3   5
result| 3   5   8  13

```
For every `n` greater than `2`, each `result` is equal to sum of results for `(n-1)` and `(n-2)`.

For every next `n`:
    - the `n-1` is equal to the previous `result`
    - the `n-2` is equal to the previous `n-1`

This can be converted into an algorithm *without* using a hashmap.

Speed: this was *incredibly* fast and efficient (**94%**, **96%**).

Complexity:
- Time: traverse each number from `1` to `n` once -> `O(n)`
- Space: same storage no matter the value of `n` -> `O(1)`

### Failed Method 1: Left/Right Sum w/Hashing

The first `5` numbers can be pictured as follows:
```
n   ct   arrangments
1   1   1
2   2   1,1         2
3   3   1,1,1       2,1           1,2
4   5   1,1,1,1     2,1,1       1,1,2     1,2,1     
5   8   1,1,1,1,1   2,1,1,1   1,1,1,2   1,1,2,1   1,2,1,1,  2,1,2   2,2,1   1,2,2
```

*Note*: this failed, but is useful because (a) the logic is sound and (b) it provides the correct answers.

Looking at the visualization above, some patterns begin to emerge:
1. Each new `number` appends `1` to the left and right for every combination in `number - 1`.
    - for `3`, take all values in `2` and append `1` to either side
2. Each new `number` appends `2` to the left and right for every combination in `number - 2`.
    - for `3`, take all values in `1` and append `2` to either side
3. To ensure unique combinations, use some form of deduplication (e.g. a `set`) is needed.

This allows for an approach using `list`s and `set`s, that fails only due to using too much memory.  Perhaps there's a better way?

### Failed Method 2: Recursive Sum

Similar to method 3, but uses recursion.

Complexity:
- Time: traverse each number from `1` to `n` once -> `O(n)`
- Space: same storage no matter the value of `n` -> `O(1)`

## Results (Python 3)

**Method 1**:  26 ms, 13.8 MB (**97.4%**, **95.96%**)

**Method 2**:  49 ms, 13.9 MB (28.16%, 12.17%)

**Method 3**:  27 ms, 13.7 MB (**94.89%**, **96.62%**)

**Failed Method 1**:  Failed - Memory Limit Exceeded

**Failed Method 2**:  Failed - Memory Limit Exceeded

## Pitfalls and Lessons Learned
1. There's always a pattern:  once you visualize a pattern, the solution becomes far more obvious.
2. Look for deeper patterns:  
3. Python's `list` and `collections.deque` are not hashable:  need to use a tuple inside of the dictionary. Just convert to/from (a) `list` to `tuple` or  (b) `deque` to `tuple`.
4. Python automatically converts single-value `tuple`s into the contained value: `(1)` is automatically coerced into `1`, `("fun")` into `"fun"`, etc.  This caused quite a headache while I was trying my solution.

Appending left and right with tuples:
```python
tuple_1 = (1,1,1)
tuple_left = tuple([2] + list(tuple_1))     # tuple_left is now (2,1,1,1)
tuple_right = tuple(list(tuple_1) + [2])    # tuple_right is now (1,1,1,2)
```
