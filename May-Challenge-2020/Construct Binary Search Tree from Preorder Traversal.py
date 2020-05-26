# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def add_node(self, root: TreeNode, ele):
        if(ele < root.val):
            if(root.left):
                self.add_node(root.left, ele)
                return
            node = TreeNode(ele)
            root.left = node
        else:
            if(root.right):
                self.add_node(root.right, ele)
                return
            node = TreeNode(ele)
            root.right = node
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if (len(preorder) > 0):
            ele = preorder[0]
        root = TreeNode(ele) 
        for i in range(1, len(preorder)):
            self.add_node(root, preorder[i])
        return root
