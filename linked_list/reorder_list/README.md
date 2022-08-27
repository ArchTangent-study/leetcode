# Reorder List ([L143](https://leetcode.com/problems/reorder-list/))
Difficulty: **Medium**

## Problem

You are given the head of a singly linked-list. The list can be represented as:
```
L0 → L1 → … → Ln - 1 → Ln
```
*Reorder the list to be in the following form*:
```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Constraints:
- The number of nodes in the list is in the range `[1, 5 * 10⁴]`.
- `1 <= Node.val <= 1000`

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Lists of length `1` and `2`
- Knowing when to stop "swapping" the list / how many swaps to perform

Number of replacements (swaps) by list length:
```
length  swaps
1       0
2       0
3       1
4       1
5       2
6       2
```

## Procedure

### Method 1: Pointer Stack and Swap

Key Idea: use a `stack` to store `Nodes` and track the number of swaps to perform

Big Picture:
1. Gather all `Nodes` into a `stack` (list)
2. Count number of `swaps` to be peformed: `(len(stack) - 1) // 2` (min: `0`)
3. While there are still `swaps` to be performed:
    - `pop()` the stack to get active `tail` pointer
    - copy the `current.next` (starts as `head`) for later use
    - set `current.next` to `tail`
    - set the copied `current.next` as the new `current` `Node`, and repeat
4. After all `swaps` are done: set `tail.next` to `None`

Complexity:
- Time: Traverse entire list to gather pointers -> `O(n)`
- Space: Gather all pointers in a stack -> `O(n)`

## Results (Python 3)

**Method 1**: 155 ms, 23.9 MB (35.31%, 64.37%)
