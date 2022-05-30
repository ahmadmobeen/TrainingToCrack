# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        ### Recursive
        left_stack = []
        right_stack = []
        print(self.left_subtree(root.left, left_stack), self.right_subtree(root.right, right_stack))
        
        return self.left_subtree(root.left, left_stack) == self.right_subtree(root.right, right_stack)
        
        
    def left_subtree(self, root, stack):
        
        if root:
            stack.append(root.val)
            print(root.val)
            self.left_subtree(root.left, stack)
            self.left_subtree(root.right, stack)
        else:
            stack.append(None)
        return stack

    def right_subtree(self, root, stack):
        
        if root:
            stack.append(root.val)
            self.right_subtree(root.right, stack)
            self.right_subtree(root.left, stack)
        else:
            stack.append(None)
        return stack
