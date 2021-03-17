class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # child nodes would be located to the left of the root element by sorting
        arr.sort()
        self.trees = {}
        #every node itself is a tree and can form len(arr) trees
        for a in arr:
            self.trees[a] = 1
        for idx, num in enumerate(arr):
            self.checkChildNodes(arr[:idx+1], idx, num)
        return sum(self.trees.values()) % (pow(10, 9)+7)
        
     # for every root node, check for all the child nodes combination whose product is equal to the root value
    def checkChildNodes(self, arr, rootIdx, root):
        nodeIdx = 0
        while nodeIdx != rootIdx:
            childNode = arr[nodeIdx]
            if root % childNode == 0 and self.trees.get(root//childNode):
                self.trees[root] += (self.trees[childNode] * self.trees[root//childNode])
            nodeIdx += 1
