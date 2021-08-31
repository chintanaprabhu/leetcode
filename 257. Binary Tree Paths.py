# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.allPaths = []
        self.helper(root, "")
        return self.allPaths
    
    def helper(self, node, path):
        if not node:
            return
        path += str(node.val)
        if not node.left and not node.right:
            self.allPaths.append(path)
        else:
            path += "->"
            self.helper(node.left, path)
            self.helper(node.right, path)
