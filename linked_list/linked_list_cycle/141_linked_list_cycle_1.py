# type: ignore

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:        
        if head is None:
            return False
        
        # Store set of pointers found
        pointers_found = set()
    
        current = head
        
        while current is not None:
            if current in pointers_found:
                return True
            pointers_found.add(current)
            
            current = current.next
        
        # If no duplicate found, there's no cycle
        return False
        