# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            newLeft = TreeNode(v, root, None)
            newLeft.left = root
            newLeft.right = None
            root = newLeft
            return root
        from collections import deque
        queue = deque()
        queue.append([root, 1])
        levelNodes = []
        while queue:
            node, depth = queue.popleft()
            if depth == d-1:
                levelNodes.append(node)
            if node.left:
                queue.append([node.left, depth+1])
            if node.right:
                queue.append([node.right, depth+1])
        for node in levelNodes:
            print(node.val)
            newLeft = TreeNode(v, node.left, None)
            newLeft.left = node.left
            node.left = newLeft
            newRight = TreeNode(v, None, node.right)
            node.right = node.right
            node.right = newRight
        return root
                    
