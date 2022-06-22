# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        prev = None
        
        while current:
            tmp_next = current.next
            current.next = prev
            prev = current
            current = tmp_next
        return prev
        
       ''' 
        new_list = ListNode(0)
        new_list.next = None
        
        current = head

        nodes_list = []
        
        if not head:
            return None
        
        while current:
        
            nodes_list.append(current)
            current = current.next

        for i in range(len(nodes_list)-1, -1, -1):
            if not new_list.next:
                new_list = nodes_list[i]
                new_ptr = new_list
            new_ptr.next = nodes_list[i]
            new_ptr = new_ptr.next
        
        
        new_ptr.next = None
        
        return new_list
        '''
