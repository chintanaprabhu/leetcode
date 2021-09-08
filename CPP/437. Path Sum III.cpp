/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int pathSum(TreeNode* root, int sum) {
        if(root == NULL)
            return 0;
        return helper(root, sum, 0) 
             + pathSum(root->left, sum) 
             + pathSum(root->right, sum);
    }
    int helper(TreeNode* root, int sum, int prev) {
        if(root == NULL)
            return 0;
        return (prev+root->val == sum) 
             + helper(root->left, sum, prev+root->val)
             + helper(root->right, sum, prev+root->val);
         }
};

/*Explanation:
1. start from the root node to explore all the paths with the given sum. 
Whenever the sum of the path is equal to the given sum, the number of paths is increased by 1.
2. The tree is traversed considering every node to be the root node and check if it leads to 
any path summing upto the given sum.*/

//====================One pass solution using map================================//

class Solution {
public:
    int help(TreeNode* root, int sum, unordered_map<int, int>& store, int pre) {
        if (!root) 
            return 0;
        root->val += pre; //update every node with the sum of the node + all ancestors
        int res = (root->val == sum) 
                + (store.count(root->val - sum) ? store[root->val - sum] : 0);
        //if the sum until a particular node is equal to the expected sum OR if the updated 
        //tree has a node whose value equals root->val - sum, indicates that a path 
        //exists below that node for the expected sum.
        store[root->val]++; // number of times a node with that sum has been visited
        res += help(root->left, sum, store, root->val) 
            + help(root->right, sum, store, root->val);
        //traverse the tree using DFS traversal
        store[root->val]--;
        //change the store counter once the particular node's children have been visited.
        //If the store looks for a value (root->val - sum), which might happen to be equal to 
        //the already visited node, we would get wrong path existence.
        return res;
    }

    int pathSum(TreeNode* root, int sum) {
        unordered_map<int, int> store;
        return help(root, sum, store, 0);
    }
};
