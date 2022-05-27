# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = []
        next = head
        while next is not None:
            values.append(next.val)
            next = next.next
        return values == values[::-1]
        # if len(values) % 2 == 0:
        #     return values[:int(len(values)/2)] == values[int(len(values)/2):][::-1] or len(values) == 1
        # else:
        #     return values[:int(len(values)/2)] == values[int(len(values)/2)+1:][::-1] or len(values) == 1
