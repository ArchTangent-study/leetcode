# Linked List Cycle ([LC141](https://leetcode.com/problems/linked-list-cycle/))
Difficulty: **Easy**

## Problem

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints:
- `The number of the nodes in the list is in the range [0, 10⁴]`.
- `-10⁵ <= Node.val <= 10⁵`
- `pos` is `-1` or a **valid index** in the linked-list.

## Thought Process

Questions:
- How do you know when a cycle is repeated?
- Can you just check to see if a pointer has been repeated?
- does `pos` act as a pointer?
- Does each `Node` have a unique `val`?  

Edge Cases / Caveats / Pitfalls:
- Empty list (`head` is `null`)

## Procedure

### Method 1: Set Membership Check

The simplest method that came to mind.  
1. If `head` is `null`, return `false`.
2. Create a `set` of `ListNode` pointers.
3. Traverse the linked list from `head`.
4. If the `ListNode` is in the `set`, return `true` (there's a cycle).
5. Add the `ListNode`'s pointer to the `set`.
6. If the entire list is traversed without finding a duplicate, return `false`.

Complexity:
- Time: all nodes are traversed once (plus one) -> `O(n)`
- Space: all nodes stored once -> `O(n)`

## Results (Python 3)

**Method 1**: 57 ms, 17.9 MB (86.32%, 9.95%)
