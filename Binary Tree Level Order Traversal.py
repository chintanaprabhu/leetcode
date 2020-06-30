# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [(root, 0)]
        curr_depth = 0
        level = []
        result = []
        while queue:
            node, dep = queue.pop(0)
            if dep != curr_depth:
                result.append(level)
                level = []
                curr_depth = dep
            if node:
                level.append(node.val)
                queue.append((node.left, dep+1))
                queue.append((node.right, dep+1))
        return result
