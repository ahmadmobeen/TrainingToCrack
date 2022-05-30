# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert(root)
      
#         newTree = TreeNode(0)
#         node = root
#         new_node = newTree
#         new_node.val = node.val

#         while True:
#             if node:
#                 new_node.left = node.right
#                 new_node.right = node.left
#                 node = node.left
#                 new_node = new_node.right
#             else:
                
#                 break


#         return newTree


        ### Recursive
        
    
    def invert(self, node):
        if node:
            tmp = node.left
            node.left = node.right
            node.right = tmp
            self.invert(node.left)
            self.invert(node.right)
            
        return node
