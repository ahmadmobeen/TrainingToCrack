# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # return self.recursive_maxDepth(root)
        # return self.iterative_BFS(root)
        return self.iterative_DFS(root)
    
    
    ### Iterative - DFS - Pre-Orer Traversal (because it is the most easy) 
    def iterative_DFS(self, root):

        stack = [[root, 1]]
        res = 0
        
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
    
    ### Iterative - BFS
    
    def iterative_BFS(self, root):
        level = 0
        if not root:
            return 0
        q = deque([root])
        while q:
            
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1
        return level
    
    ### Recursive - DFS
    
    def recursive_maxDepth(self, root):
        
        if not root:
            return 0
        else:
            return 1 + max(self.recursive_maxDepth(root.left), self.recursive_maxDepth(root.right))
    
    
        

#         node = root
#         num_nodes = 0
#         max_depth = 0
#         stack = []
#         while True:
#             if node:
#                 num_nodes += 1
#                 stack.append(node)
#                 node = node.left
#                 if num_nodes > max_depth:
#                     max_depth = num_nodes
#             else:
                
#                 if len(stack) != 0:
#                     node = stack.pop()
                    
#                     node = node.right
                
                   
#                 else:
#                     break
#         return max(num_nodes, max_depth)
