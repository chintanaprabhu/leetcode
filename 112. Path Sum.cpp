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
    bool hasPathSum(TreeNode* root, int sum) {
       if(root == NULL) 
           return false;
        
      /*  sum -= root->val;
       if(root->left == NULL && root->right == NULL)
           return (sum == 0);
        return (hasPathSum(root->left, sum) || 
                hasPathSum(root->right, sum));*/
        
        ///////Iterative solution//////////////////
        stack<TreeNode*> nodes;
        stack<int> rem_sum;
        nodes.push(root);
        rem_sum.push(sum - root->val);
        
        TreeNode* node;
        int curr_sum;
        
        while(!nodes.empty()) {
            node = nodes.top();
            nodes.pop();
            curr_sum = rem_sum.top();
            rem_sum.pop();
            if( node->right == NULL && node->left == NULL && curr_sum == 0)
                return true;
            
            if(node->right != NULL) {
                nodes.push(node->right);
                rem_sum.push(curr_sum - node->right->val);
            }
            if(node->left != NULL) {
                nodes.push(node->left);
                rem_sum.push(curr_sum - node->left->val);
            }
        }
        return false;
    }
};
