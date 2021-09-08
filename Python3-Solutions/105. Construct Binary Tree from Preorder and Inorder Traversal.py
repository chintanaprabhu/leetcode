# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #index to access elements of preorder without slicing
        self.root_index = 0
        #transform inorder into dict to extract index of every element
        #index is used to determine the left and right subtree elements
        valIdx = {val:idx for idx, val in enumerate(inorder)}
        
        def helper(left, right):
            #base case
            if left > right:
                return
            
            val = preorder[self.root_index]
            root = TreeNode(val)
            self.root_index += 1
            #determine the index of node and separate inorder into left and right subtrees
            nodeIdx = valIdx[val]
            #recursively build left and right sub trees
            root.left = helper(left, nodeIdx-1)
            root.right = helper(nodeIdx+1, right)
            return root
        
        return helper(0, len(inorder)-1)
        
######################short solution##############
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.root_index = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            nodeIdx = inorder.index(preorder[self.root_index])
            self.root_index += 1
            root = TreeNode(inorder[nodeIdx])
            root.left = self.buildTree(preorder, inorder[:nodeIdx])    
            root.right = self.buildTree(preorder, inorder[nodeIdx+1:])
            return root
        
