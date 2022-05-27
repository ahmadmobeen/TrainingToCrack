# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        current1 = list1
        current2 = list2
        
        final_head = ListNode(0)
        
        if not current1:
            final_head = current2
            return final_head

        elif not current2:
            final_head = current1
            return final_head
            
        if current1.val > current2.val:
            final_head = current2
            current2 = current2.next
        else:
            final_head = current1
            current1 = current1.next
        
        final_ptr = final_head

        while current1 or current2:
            if not current1:
                final_ptr.next = current2
                return final_head

            elif not current2:
                final_ptr.next = current1
                return final_head
            
            if current1.val > current2.val:
                
                final_ptr.next = current2
                current2 = current2.next
                final_ptr = final_ptr.next
            
            else:
                final_ptr.next = current1
                current1 = current1.next
                final_ptr = final_ptr.next

        return final_head
