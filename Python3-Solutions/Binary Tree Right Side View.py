# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return
        queue = collections.deque()
        queue.append([root, 0])
        rightView = []
        while queue:
            node, NodeLevel = queue.popleft()
            if node.left:
                queue.append([node.left, NodeLevel+1])
            if node.right:
                queue.append([node.right, NodeLevel+1])
            if queue and queue[0][1] != NodeLevel:
                rightView.append(node.val)
        #add last node of lsat level
        rightView.append(node.val)
        return rightView
            
