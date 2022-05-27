# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        
        ### with hashmap 
        hashmap = {}
   
        currentA = headA
        while currentA:
            
            hashmap[currentA] = currentA.val
            currentA = currentA.next
      
        currentB = headB
        while currentB:
            if currentB in hashmap.keys():
                return currentB

            currentB = currentB.next
        
        ### x in list -> O(n)
        ### x in dict -> O(1)
        ## time out
#         hashmap = []
#         i = 0
#         currentA = headA
#         while currentA:
            
#             hashmap.append(currentA)
#             currentA = currentA.next
#             i += 1
            
#         currentB = headB
#         while currentB:
#             if currentB in hashmap:
#                 return currentB
#                 # if currentB == hashmap[currentB.val]:
#                 #     return currentB
#             currentB = currentB.next
        
        


        
        
        
        
        
        
        ## Time limit exceeded
#         hashmap = {}
#         i = 0
#         currentA = headA
#         while currentA:
#             hashmap[i] = currentA
#             currentA = currentA.next
#             i += 1
            
#         currentB = headB
#         while currentB:
#             for i in range(len(hashmap)):
#                 if currentB == hashmap[i]:
#                     return currentB
#             currentB = currentB.next

            
        
        
        ## Time limit exceeded O(NxM) complexity (i guess)
#         currentA = headA
        
#         while currentA:
    
#             currentB = headB            # Start again from headB
#             while currentB:         # Keeping one linkedlist at one node while iterating the other node

#                 if currentA == currentB: # If the nodes intersect
#                     return currentA
                
#                 currentB = currentB.next
#             currentA = currentA.next
        

    ##Time limit exceeded
    
#         currentA = headA
#         currentB = headB
#         while True:
            
#             if currentA == currentB:
#                 return currentA
            
#             currentA = currentA.next if currentA else headA
            
#             currentB = currentB.next if currentB else headB
            
#             if currentA == headA and currentB == headB:
#                 break
#             else:
#                 continue
