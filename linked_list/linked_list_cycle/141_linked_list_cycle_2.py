# type: ignore

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:        
        # Slow pointer advances one node at a time
        # Fast pointer advances two nodes at a time
        slow = head
        fast = head
        
        # Check fast for None, as it will reach none sooner
        while fast is not None:
            if fast.next is None:
                return False
            
            fast = fast.next.next
            slow = slow.next
            
            # If fast pointer cycles, it will catch up to slow
            if fast == slow:
                return True
        
        # List traversed w/o duplicate found -> no cycle
        return False
    