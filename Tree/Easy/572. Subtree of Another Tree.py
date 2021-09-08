# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. Using explicit stack and DFS on every match of root.val and subRoot.val
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if self.checkSubtree(node, subRoot):
                    return True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return False

# stack state
#    [3] => 3
#    [5, 4] => 4
#    [5, 2, 1] => 1
#    [5, 2] => 2
#    [5] => 5

# 2. Using recursion on tree and subtree.
# 3 cases: a. tree == subTree
#          b. tree.left == subTree
#          c. tree.right == subTree

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val and self.checkSubtree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
      
# helper function to check node match

    def checkSubtree(self, root, subroot):
        if not root and not subroot:
            return True
        if root and subroot:
            if root.val != subroot.val:
                return False
            if self.checkSubtree(root.left, subroot.left) and self.checkSubtree(root.right, subroot.right):
                return True
        return False
        
