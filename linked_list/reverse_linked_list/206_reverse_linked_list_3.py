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
            # Swap values using original node.next as a temp value
            original_next = current.next
            current.next = previous
            # Prepare to move to next node
            previous = current
            current = original_next
        
        return previous
        