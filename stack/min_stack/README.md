# Min Stack ([LC155](https://leetcode.com/problems/min-stack/))
Difficulty: **Easy**

## Problem

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element val onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

Constraints:
- `-2³¹ <= val <= 2³¹ - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks.
- At most `3 * 10⁴` calls will be made to `push`, `pop`, `top`, and `getMin`.

## Thought Process

*Note*: ask lots of questions to make sure you fully understand the requirements!

The trick to this problem is figuring out how to both:
- `pop()` *and*
- retrieve minimum element in `O(1)` time via `getMin()`

Edge Cases / Pitfalls / Caveats:
- Keeping track of minimum value after poppling values

Approaches:
1. Since there's no space complexity requirement, you can *use two lists*, one for popping the top element, and one for getting the minimum element.
2. You can pair the minimum value at a given point in time by using a *single list of 2-tuples*, with one value for the stack, and another for the current minimum.

## Procedure

### Method 1: Tuple Stack

Uses a `(stack_val, min_val)` 2-tuple for the `stack`.

The `min_val` stores the minimum value *at the time the value was added to the stack*.  So when a value is `pop()`ped from the stack, the minimum value will always be the `min_val` of the topmost tuple in the stack.

This method isn't particularly fast, but it's reasonably intuitive.

## Results (Python 3)

**Method 1**:  111 ms, 18.5 MB (34.09%, 13.37%)
