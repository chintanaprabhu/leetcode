# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, targetSum, 0)
    
    def helper(self, root, targetSum, curSum):
        if not root:
            return 0
        if root.left is None and root.right is None:
            return root.val+curSum == targetSum
        return self.helper(root.left, targetSum, curSum+root.val) or self.helper(root.right, targetSum, curSum+root.val)
        
        
