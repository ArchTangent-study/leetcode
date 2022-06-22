# type: ignore

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Key Idea: compare main list's `next` node vs side list's `current` node."""
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            head = list1
            a = list1.next
            b = list2
        else:
            head = list2
            a = list2.next
            b = list1

        # Tracks the most recent pointer in the merged list
        seek = head

        # Append values to head (seek) as long as either list still has values
        while a and b:
            # 'seek' values are lookahead placeholder pointers.
            a_seek, b_seek = a.next, b.next
            # If A < B, set seek to A and advance A
            if a.val < b.val:
                seek.next = a
                a = a_seek
            # B <= A, set seek to B and advance B
            else:
                seek.next = b 
                b = b_seek
            # Advance seek
            seek = seek.next

        # Append any remaining values in 'A' or 'B' to 'seek'
        if a:
            seek.next = a
        if b:
            seek.next = b

        return head
