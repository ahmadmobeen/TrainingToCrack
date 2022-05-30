######## Fastest method - Adopted from https://github.com/goldshakil/Coding_Interview_Preparation/blob/master/LeetCode/Python/python_155.py #####


class MinStack:

    def __init__(self):
        self.stack = []
        self.minArr = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.minArr) == 0:
            self.minArr.append(val)
        else:
            if self.minArr[-1] > val:   ### original -> self.minArr[-1] >= val
                self.minArr.append(val)
            else:
                self.minArr.append(self.minArr[-1])

        
    def pop(self) -> None:
        val = self.stack.pop()
        
        ### Remove the self.stack.pop value from minArr
        self.minArr.pop()
                
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # return min(self.stack) # O(n)
        return self.minArr[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



####### Accepted Solution at leetcode. This code keeps track of all the elements of stack by creating an array with all the stack elements in descending order. ###########
# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.minArr = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
        
#         if len(self.minArr) == 0:
#             self.minArr.append(val)
#         else:
#             if self.minArr[-1] > val:
#                 self.minArr.append(val)
#             else:
#                 tmp_minArr = []
#                 while len(self.minArr) !=0 and val > self.minArr[-1]:   ## Empty the minArr in a temp list until the new value is higher than the
#                                                                         ## minArr top    
#                     tmp_minArr.append(self.minArr.pop())     

#                 self.minArr.append(val)                                 ## Append the new value in minArr
#                 while len(tmp_minArr) != 0:                         
#                     self.minArr.append(tmp_minArr.pop())                ## Empty the empty array back in minArr
        
#     def pop(self) -> None:
#         val = self.stack.pop()
        
#         for i in range(len(self.minArr)):   #### Find the location of the self.stack.pop value in minArr
#             if val == self.minArr[i]:
#                 while i < len(self.minArr)-1:
#                     self.minArr[i] = self.minArr[i+1]
#                     i += 1
#                 break
        
#         ### Remove the self.stack.pop value from minArr
#         self.minArr.pop()
                
        

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         # return min(self.stack) # O(n)
#         return self.minArr[-1]
        

######### Using Python's min() funtion. Accepted solution at Leetcode but min() is O(n) ##################

# class MinStack:
#     # Simple solution with using Python List
#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)

#     def pop(self) -> None:
#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
