# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #modify the definition for recursive call
    def sumNumbers(self, root: TreeNode, tree_num = 0) -> int:
        #base case
        if root is None:
            return 0
        else:
            #update the root_to_leaf sum for every node as we traverse down the level
            tree_num = 10 * tree_num + root.val
            #update the total root_to_leaf sum when a leaf node is encountered
            if root.left is None and root.right is None:
                return tree_num
            else:
                #recursive invoke sumNumbers for child nodes
                return self.sumNumbers(root.left, tree_num) + self.sumNumbers(root.right, tree_num)
            
