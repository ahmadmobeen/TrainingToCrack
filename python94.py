# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        # return self.dfs_recursive(root, res)
        return self.dfs_iterative(root, res)
        
    
    ###### Iterative - Inorder
    def dfs_iterative(self, node, res):
        stack = []
            
        # check if node -> left exists
        while True:
            if node:
                stack.append(node)
                node = node.left
        
            else:
                if len(stack) != 0:
                    node = stack.pop()
                    res.append(node.val)
                    node = node.right
                else:
                    break
        return res
        

    ###### Recursive - Inorder
    def dfs_recursive(self, node, res):
        if node:

            self.dfs_recursive(node.left, res)
            res.append(node.val)
            self.dfs_recursive(node.right, res)
        
        return res
