# Set Matrix Zeroes ([LC073](https://leetcode.com/problems/set-matrix-zeroes/))
Difficulty: **Medium**

## Problem

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`s.

You must do it **in place**.

Constraints:
- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2³¹ <= matrix[i][j] <= 2³¹ - 1`

Follow up:
- A straightforward solution using `O(mn)` space is probably a bad idea.
- A simple improvement uses `O(m + n)` space, but still not the best solution.
- Could you devise a constant space (`O(1)`) solution?

## Thought Process

Edge Cases / Caveats / Pitfalls:
- `m` or `n` equal to `1`
- get entire `row` and `col`, not just neighbors

Ideas:
- convert entire rows and columns *at once*

## Procedure

### Method 1: Two-Pass Delayed Zeroization with Row/Col Set

Key Idea: use two sets, and two passes over the `matrix`.

Big Picture:
1. Use set of rows/columns to be converted (`rows_to_zeroize`, `cols_to_zeroize`)
2. First pass finds the row/col of any zero values
3. Second pass traverses:
    - each `col` for every `row` in `rows_to_zeroize`
    - each `row` for every `col` in `cols_to_zeroize`
    - and sets each `(row,col)` value in `matrix` to `0`

Complexity:
- Time: Two passes -> `O(2(m * n))` -> `O(m * n)`
- Space: `O(m + n)`

Thoughts: this was ***incredibly*** fast despite not being optimally space efficient.

### Method 2: Two-Pass Delayed Zeroization with Row/Col Set

Key Ideas:
- Works like *Method 1*, but uses a `list` instead of a `set`.  Transitions nicely into the follow-up approach (*Method 3*).
- Can also use `bool` values instead of `1`s or `0`s.  Can be more space efficient in some languages.

Complexity:
- Time: Three passes (inc. one to initialize lists) -> `O(3(m * n))` -> `O(m * n)`
- Space: `O(m + n)`

### Method 3: Two-Pass In-Place Zeroization (Follow-Up)

Key Idea: build upon *Method 2* by using the *first row* and *first column* in the same capacity as the separate `list`s used in *Method 2*.  To account for the overlapping of the `0`th values in `row 0` and `col 0`, use a separate `bool` to represent `row 0` called `row_0_zeroized`.

Complexity:
- Time: Two passes -> `O(2(m * n))` -> `O(m * n)`
- Space: `O(1)`

*Caveat*: need to zeroized `row 0` (via `row_0_zeroize` `bool`) *after* zeroizing each `col`. Otherwise, the newly-zeroized `row 0` values will "contaminate" the coluumn computation.

## Results (Python 3)

**Method 1**:  119 ms, 14.7 MB (**99.78%**, **90.66%**)

**Method 2**:  144 ms, 14.8 MB (84.01%, 53.16%)

**Method 3**:  171 ms, 14.9 MB (54.1%, 17.4%)
