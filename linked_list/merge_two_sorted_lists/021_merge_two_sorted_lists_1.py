# type: ignore
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Choose lowest of lists as head for merged list    
        # Set seek equal to head to avoid using a separate dummy node      
        if list1.val <= list2.val:
            head = list1
            seek = head
            alt = list2
        else:
            head = list2
            seek = head
            alt = list1
            
        while seek is not None and alt is not None:
            # Advance seek pointer while its values are less than node in side list
            while seek.next is not None and seek.next.val < alt.val:
                seek = seek.next
            # Swap lists
            seek.next, alt = alt, seek.next
            seek = seek.next         
        
        return head
