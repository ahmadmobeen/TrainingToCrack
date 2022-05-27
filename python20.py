def is_left_brace(s):
    if s == '[' or s == '{' or s == '(':
        return True
    return False
def top(stack):
    return stack[-1]

class Solution:
    
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            
            if is_left_brace(ch) or len(stack) == 0:
                stack.append(ch)
                
            else:
                if ch == ')' and top(stack) == '(':
                    stack.pop()
                elif ch == ']' and top(stack) == '[':
                    stack.pop()
                elif ch == '}' and top(stack) == '{':
                    stack.pop()
                    
                else:
                    return False
        if len(stack) == 0:
            return True
        
        return False
                    
