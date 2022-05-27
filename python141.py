# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    
    # O(N) solution, O(1) space Floyd's cycle detection algorithm (Tortoise and Hare)
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head == None:
            return False
        current = head
        jumper = head
        while jumper and jumper.next: # this sequence is important, "jumper.next and jumper" will cause a runtime error.
            
            jumper = jumper.next.next
            current = current.next
            
            if jumper == current:
                return True
        return False
