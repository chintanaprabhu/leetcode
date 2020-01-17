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
