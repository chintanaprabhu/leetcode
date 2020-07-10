# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        from collections import deque
        #maintain a queue of every node and it's corresponding serial number starting from 1
        queue = deque([ (root, 1) ]) if root else [ ]
        maxWidth = 0
        while queue:
            #check the maxWidth as levels are traversed
            l, r = queue[0][1], queue[-1][1]
            maxWidth = max(maxWidth, r-l+1)
            
            #at every level add the non-null nodes along with the serial num to the queue
            for i in range(len(queue)):
                node, val = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*val))
                if node.right:
                    queue.append((node.right, 2*val + 1))
        return maxWidth
