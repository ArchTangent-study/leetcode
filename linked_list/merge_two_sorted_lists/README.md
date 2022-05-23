# Merge Two Sorted Lists ([LC021](https://leetcode.com/problems/merge-two-sorted-lists/))
Difficulty: **Easy**

## Problem

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return the *head of the merged linked list*.

Constraints:
- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order.

## Thought Process

Edge Cases / Caveats / Pitfalls:
- Cases where values are equal to each other (`<=` cases)
- "Orphaning" a node while splicing (use copies)
- Uneven list lengths
- Null lists
- When to stop splicing (exit point)
- Preserving the initial pointer of the answer (`head`)

## Procedure

### Method 1: Seek and Swap

## Results (Python 3)

**Method 1**: 39 ms, 13.8 MB (85.48%, 79.41%)
