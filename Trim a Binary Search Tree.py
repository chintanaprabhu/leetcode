# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return
        if root.val < low:
            # trim the current root along with its left subtree
            # as all the elements to the left of current root 
            # are going to be lesser than low
            return self.trimBST(root.right, low, high)
        if root.val > high:
            #trim the current root along with its right subtree 
            # as all the elements to the right of current root 
            # are going to be greater than low
            return self.trimBST(root.left, low, high)
        # if node value is within the range of low, high
        # recursively call trimBST for its left and right subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
