# type: ignore
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle cases with zero or no node
        if head is None or head.next is None:
            return head
        
        # At least one node -> recursively reverse nodes
        return self.reverseNodes(head, None)
        
    def reverseNodes(self, node: ListNode, prev: Optional[ListNode]) -> ListNode:
        # If next node is None, you're at the end, return node
        if node.next is None:
            node.next = prev
            return node
        
        # Otherwise reverse w/temporary values and recursively call
        original_next = node.next
        node.next = prev
        
        return self.reverseNodes(original_next, node)
        