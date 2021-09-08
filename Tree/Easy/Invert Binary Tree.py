# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        from queue import Queue.  #using Queue class
        temp_node = root
        q = Queue()
        q.put(root)
        while not q.empty():
            temp_node = q.get()
            if temp_node:
                temp_node.left, temp_node.right = temp_node.right, temp_node.left
                q.put(temp_node.left)
                q.put(temp_node.right)
        return root
########################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def invertTree(self, root: TreeNode) -> TreeNode:
        temp_node = root
        queue=[root]   #using a list as queue
        while(queue):
            temp_node = queue.pop(0). #expensive operation!
            if temp_node:
                temp_node.left, temp_node.right = temp_node.right, temp_node.left
                queue.append(temp_node.right)
                queue.append(temp_node.left)
        return root
