# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1. iterative DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if not root:
            return depth
        stack = [(root, 1)]
        while stack:
            node, d = stack.pop()
            if not node.left and not node.right:
                depth = max(depth, d)
            if node.right:
                stack.append((node.right, d+1))
            if node.left:
                stack.append((node.left, d+1))
        return depth
      

#2. recursive DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
                
                
