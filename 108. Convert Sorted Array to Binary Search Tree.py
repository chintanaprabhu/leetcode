# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 1.  create the first node and 
    #     recursively divide left and right sub arrays to form left and right subtrees
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        allNums = len(nums)
        mid = allNums // 2
        root = TreeNode(nums[mid])
        leftSubtree = nums[:mid]
        rightSubtree = nums[mid+1:]
        self.helper(root, leftSubtree, rightSubtree)
        return root
    
    def helper(self, node, leftSubtree, rightSubtree):
        if leftSubtree:
            leftMid = len(leftSubtree) // 2
            node.left = TreeNode(leftSubtree[leftMid])
            self.helper(node.left, leftSubtree[:leftMid], leftSubtree[leftMid+1:])
        if rightSubtree:
            rightMid = len(rightSubtree) // 2
            node.right = TreeNode(rightSubtree[rightMid])
            self.helper(node.right, rightSubtree[:rightMid], rightSubtree[rightMid+1:])
     
    # 2. divide and conquer top-down tree constructed
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
          return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
  
