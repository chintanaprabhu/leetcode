# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.sumHelper(root, low, high)
    
    def sumHelper(self, node, low, high):
        if not node:
            return 0
        # prune left subtree
        if node.val < low:
            return self.sumHelper(node.right, low, high)
        # prune right subtree
        elif node.val > high:
            return self.sumHelper(node.left, low, high)
        else:
            return node.val + self.sumHelper(node.left, low, high) + self.sumHelper(node.right, low, high)
