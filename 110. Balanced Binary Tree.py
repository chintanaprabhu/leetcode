# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Top-down recursion - O(nlogn)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.getHeight(root.left) - self.getHeight(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getHeight(self, root):
        if not root:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        return max(left, right) + 1

# Bottom-up recursion with early termination - O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkBalance(root)[0]
    
    def checkBalance(self, root):
        if not root:
            return (True, 0)
        leftBalance, lHeight = self.checkBalance(root.left)
        rightBalance, rHeight = self.checkBalance(root.right)
        if not leftBalance or not rightBalance or abs(lHeight - rHeight) > 1:
            return (False, max(lHeight, rHeight) + 1)
        return (True, max(lHeight, rHeight) + 1)
