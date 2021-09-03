# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        ans = inf
        curr = root
        prevNode = None
        while stack or curr != None:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prevNode and curr:
                ans = min(ans, abs(curr.val - prevNode.val))
            prevNode = curr
            curr = curr.right
        return ans
  
