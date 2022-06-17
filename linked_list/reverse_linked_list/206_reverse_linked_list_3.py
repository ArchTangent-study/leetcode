# type: ignore
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Store current and previous nodes
        previous = None
        current = head
        # Iterate over while loop while a non-None node exists
        while current is not None:
            # Create temporary next value
            temp_next = current.next
            # Point current to previous (reversing)
            current.next = previous
            # Push current back into previous
            previous = current
            # Replace void left by moved current with temporary next
            current = temp_next

            return previous
