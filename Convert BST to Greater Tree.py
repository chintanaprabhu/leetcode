# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# iterative
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        rootCopy = root
        if not root:
            return
        treeSum = 0
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.right
            cur = stack.pop()
            treeSum += cur.val
            cur.val = treeSum
            if cur.left:
                root = cur.left
        return rootCopy

# recursive
class Solution:
    def __init__(self):
        self.sum = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.calcSum(root)
        return root
    def calcSum(self, node):
        if node is None:
            return
        if node.right:
            self.calcSum(node.right)
        self.sum += node.val
        node.val = self.sum
        if node.left:
            self.calcSum(node.left)
