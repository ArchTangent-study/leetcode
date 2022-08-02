# Detect Squares ([LC2013](https://leetcode.com/problems/detect-squares/))
Difficulty: **Medium**

## Problem

You are given a stream of points on the X-Y plane. Design an algorithm that:
- **Adds** new points from the stream into a data structure. **Duplicate** points are allowed and should be treated as different points.
- Given a query point, **counts** the number of ways to choose three points from the data structure such that the three points and the query point form an **axis-aligned square** with **positive area**.

An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:
- `DetectSquares()` Initializes the object with an empty data structure.
- `void add(int[] point)` Adds a new point `point = [x, y]` to the data structure.
- `int count(int[] point)` Counts the number of ways to form axis-aligned squares with point `point = [x, y]` as described above.

Constraints:
- `point.length == 2`
- `0 <= x, y <= 1000`
- At most `3000` calls in total will be made to `add` and `count`.
- Each square requires a **positive area**
- Getting the *number of ways* a square can be formed

## Thought Process

Questions:
- Will any points be removed?

Edge Cases / Caveats / Pitfalls:
- Duplicate points are allowed - account for them

## Procedure

### Method 1: Paired Coaxial Values with Dict

*Note*: *read the requirements!*  It's clearly stated that a **positive area** is required.  Not accounting for this will result in errors.

Complexity:
- Add: `O(1)`
- Count: for each coaxial `x`, count pairs of matching `y` -> `O(4n²)` -> `O(n²)`
- Space: `O(n)`

Thoughts: based on the low runtime score (`5%`), there's certainly a faster approach to the `count()` method.

### Method 2: Paired Coaxial Values with Dict and Tuple Counter

Key Idea: improve speed and sacrifice space by adding a separate `(x,y)` point counter.

Complexity:
- Add: `O(1)`
- Count: directly get count of each needed `(x,y)` pair-> `O(4n)` -> `O(n)`
- Space: two dictionaries -> `O(2n)`-> `O(n)`

## Results (Python 3)

**Method 1**: 2338 ms, 15.9 MB (5.02%, 59.07%)

**Method 2**: 748 ms, 16.2 MB (26.97%, 16.79%)
