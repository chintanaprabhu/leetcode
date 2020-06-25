# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # recursive solution
        #if root == None:
        #    return 0
        #return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
       
        # iterative solution
        stack = []
        depth = 0
        if root != None:
            stack.append((1, root))
        while stack != []:
            curr_depth, node = stack.pop()
            if node != None:
                depth = max(depth, curr_depth)
                stack.append((curr_depth+1, node.left))
                stack.append((curr_depth+1, node.right))
        return depth
