# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def get_tree_depth(node):
            if node:
                return 1 + get_tree_depth(node.left)
            else:
                return 0
        def count(node):
            h = get_tree_depth(node)
            #base case handled
            if h==0:
                return 0
            #general case
            else:
                #if tree is right complete
                if h-1 == get_tree_depth(node.right):
                    return 2 ** (h-1) + count(node.right)
                else:
                    return 2 ** (h-2) + count(node.left)
        return count(root)
        
        
