# type: ignore
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseNodes(head, None)
        
    def reverseNodes(self, node: ListNode, prev: Optional[ListNode]) -> ListNode:
        # If current node is None, you're at the end, return previous
        if node is None:
            return prev
        
        # Otherwise reverse w/temporary values and recursively call
        temp_next = node.next
        node.next = prev
        
        return self.reverseNodes(temp_next, node)
