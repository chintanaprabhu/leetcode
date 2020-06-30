# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #recursive
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
        
        return isMirror(root,root)
 ###################################
class Solution:
    #iterative
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [root,root]
        while queue:
            left, right = queue.pop(0), queue.pop(0)
            if left==None and right==None:
                continue
            if left==None or right==None:
                return False
            if left.val != right.val:
                return False
            queue.append(left.right)
            queue.append(right.left)
            queue.append(left.left)
            queue.append(right.right)
        return True
                
