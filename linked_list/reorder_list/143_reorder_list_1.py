# type: ignore

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """        
        # Traverse list and gather pointers as a stack
        pointers = []
        current = head
        
        while current:
            pointers.append(current)
            current = current.next

        # Get number of swaps to perform
        swaps = max((len(pointers) - 1) // 2, 0)
        current = head

        while swaps > 0 and current is not None:       
            tail = pointers.pop()   # copy of tail
            next = current.next     # copy of next 

            current.next = tail
            tail.next = next
            current = next

            swaps -= 1

        # Set tail (last pointer in pointers)'s next to None
        if pointers:
            pointers[-1].next = None

        return None
