# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return
        from collections import deque  
        queue = deque()
        queue.append([root,0])
        curLevel = 0
        avgList = []
        levelSum = 0
        levelNodes = 0
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
            if curLevel != level:
                curLevel = level
                levelAvg = levelSum / levelNodes
                avgList.append(levelAvg)
                levelSum = 0
                levelNodes = 0
            levelNodes += 1
            levelSum += node.val
        levelAvg = levelSum / levelNodes
        avgList.append(levelAvg)
        return avgList
            
